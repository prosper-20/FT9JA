from django.urls import path
from .views import user_dashboard, login, graph_view, admin_dashboard, logout
from .utils import simulate_profit_and_loss


urlpatterns = [
    path("", user_dashboard, name="user-dashboard"),
    path("ad/", admin_dashboard, name="admin-dashboard"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("graph/", graph_view, name="graph"),
    path("simulate/", simulate_profit_and_loss, name="simulate")
]