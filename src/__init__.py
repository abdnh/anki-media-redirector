from __future__ import annotations

import re
from typing import Any

from anki import hooks
from aqt import mediasrv, mw
from aqt.mediasrv import BundledFileRequest, DynamicRequest, LocalFileRequest, NotFound

CONFIG = mw.addonManager.getConfig(__name__)
redirected_patterns = [re.compile(p) for p in CONFIG["redirected_patterns"]]


def should_redirect(path: str) -> bool:
    return any(pattern.match(path) for pattern in redirected_patterns)


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


mw.addonManager.setWebExports(__name__, r"user_files/media/.*")
mediasrv._extract_request = hooks.wrap(
    mediasrv._extract_request, redirect_media_request, "around"
)
