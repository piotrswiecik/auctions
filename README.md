# Auctions site demo

## Local development setup

Routing based on Traefik as API gateway & balancer.

- `auctions.localhost/auctions` -> routes to auction service & prepends /api to path.
- `auctions.localhost/search` -> routes to search service & prepends /api to path.
