"""Formatters for custom two1 buys."""

import json
from textwrap import wrap
from tabulate import tabulate


def search_formatter(res):
    """custom formatter for search."""
    formatted_search_results = []
    headers = ("No.", "Result")
    search_results = json.loads(res.json()['results'])['d']['results']
    for i, search_result in enumerate(search_results):
        title = search_result["Title"]
        url = search_result["Url"]
        desc = search_result["Description"]

        formatted_search_results.append([i, title])
        formatted_search_results.append(["", "-----------------"])
        formatted_search_results.append(["", url])
        for i, l in enumerate(wrap(desc, 80)):
            formatted_search_results.append(["", l])
        formatted_search_results.append(["", ""])
    return(
        tabulate(
            formatted_search_results,
            headers=headers,
            tablefmt="psql"
            )
        )


def social_formatter(res):
    """custom formatter for social."""
    message = res.json()["success"]
    return "You just sent the direct message: {}".format(message)


def content_formatter(res):
    """custom formatter for content."""
    url = res.json()["article"]
    return "You just purchased the article {}".format(url)