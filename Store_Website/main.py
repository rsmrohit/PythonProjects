import justpy as jp

from webapp.purchasing import Purchasing
from webapp.sales import Sales

jp.Route("/home", Sales.serve)
jp.Route("/purchasing", Purchasing.serve)

jp.justpy()