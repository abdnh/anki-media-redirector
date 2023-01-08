from __future__ import annotations

from pathlib import Path
from typing import Any

from anki import hooks
from anki.collection import Collection
from aqt import mediasrv, mw
from aqt.mediasrv import BundledFileRequest, DynamicRequest, LocalFileRequest, NotFound
from aqt.operations import QueryOp
from aqt.qt import *

ADDON_NAME = "Media Redirector"
REDIRECTED_MEDIA_DIR = Path(__file__).parent / "user_files" / "media"


def should_redirect(path: str) -> bool:
    return (REDIRECTED_MEDIA_DIR / path).exists()


def redirect_media_request(
    path: str,
    _old: Any,
) -> LocalFileRequest | BundledFileRequest | DynamicRequest | NotFound:
    if should_redirect(path):
        addon_path = (
            f"{mw.addonManager.addonFromModule(__name__)}/user_files/media/{path}"
        )
        return LocalFileRequest(root=mw.addonManager.addonsFolder(), path=addon_path)
    return _old(path)


def remove_redirected() -> None:
    def op(col: Collection) -> None:
        for path in Path(col.media.dir()).iterdir():
            if path.is_file() and should_redirect(path.name):
                os.remove(path)

    QueryOp(parent=mw, op=op, success=lambda _: ()).run_in_background()


mw.addonManager.setWebExports(__name__, r"user_files/media/.*")
mediasrv._extract_request = hooks.wrap(
    mediasrv._extract_request, redirect_media_request, "around"
)

menu = QMenu(ADDON_NAME)
action = QAction("Remove redirected files from collection.media")
qconnect(action.triggered, remove_redirected)
menu.addAction(action)
mw.form.menuTools.addMenu(menu)
