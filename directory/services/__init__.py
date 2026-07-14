"""Structured content modules for ServiceListiclePage instances.

Each module here corresponds to one /australia/{service}/ (or /australia/{city}/{service}/)
page and is auto-loaded by ServiceListiclePage.get_context from the page slug
(slug "emergency-dentist" -> module "emergency_dentist"). Mirrors the directory.hub_content
pattern for /australia/.
"""
