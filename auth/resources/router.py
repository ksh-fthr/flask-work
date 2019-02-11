"""
各 API のルーティングのためのモジュール
"""

from auth.resources.all_users import AllUsers
from auth.resources.login import UserLogin
from auth.resources.logout_access import UserLogoutAccess
from auth.resources.logout_refresh import UserLogoutRefresh
from auth.resources.token_refresh import TokenRefresh
from auth.resources.user_registration import UserRegistration
