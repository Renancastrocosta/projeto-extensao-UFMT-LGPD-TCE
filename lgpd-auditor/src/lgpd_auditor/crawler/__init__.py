"""Módulo de crawler."""

from lgpd_auditor.crawler.service import CrawlerService, CrawlResult
from lgpd_auditor.crawler.visited_routes import VisitedRoute, VisitedRoutesLog

__all__ = [
    "CrawlerService",
    "CrawlResult",
    "VisitedRoute",
    "VisitedRoutesLog",
]
