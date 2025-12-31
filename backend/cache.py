"""
Caching layer for Nexus.

Provides in-memory caching to avoid repeated DB queries for unchanged data.
Cache is automatically invalidated when data is modified.
"""

from typing import Any

from aiocache import Cache

# Initialize a simple in-memory cache
# TTL is set per-key when storing values
cache = Cache(Cache.MEMORY)

# Cache key prefixes for different data types
CACHE_KEYS = {
    "items_list": "items:list:{skip}:{limit}",
    "item_detail": "items:detail:{uuid}",
    "items_count": "items:count",
}

# Default TTL in seconds (5 minutes)
DEFAULT_TTL = 300


async def get_cached(key: str) -> Any | None:
    """
    Get a value from cache.

    Returns None if key doesn't exist or has expired.
    """
    return await cache.get(key)


async def set_cached(key: str, value: Any, ttl: int = DEFAULT_TTL) -> None:
    """
    Store a value in cache with TTL.

    Args:
        key: Cache key
        value: Value to cache (must be serializable)
        ttl: Time-to-live in seconds (default: 5 minutes)
    """
    await cache.set(key, value, ttl=ttl)


async def invalidate_items_cache() -> None:
    """
    Invalidate all item-related cache entries.

    Call this after any write operation (create, update, delete).
    """
    # Clear all keys - in production you'd use pattern matching
    # For now, we just clear the entire cache
    await cache.clear()


async def get_or_set(key: str, fetch_func: Any, ttl: int = DEFAULT_TTL) -> Any:
    """
    Get value from cache, or fetch and cache it if not present.

    This is the main caching pattern:
    1. Check cache for key
    2. If found, return cached value
    3. If not found, call fetch_func to get value
    4. Store result in cache
    5. Return value

    Args:
        key: Cache key
        fetch_func: Async function to call if cache misses
        ttl: Time-to-live in seconds

    Returns:
        The cached or freshly fetched value
    """
    cached_value = await cache.get(key)
    if cached_value is not None:
        return cached_value

    # Cache miss - fetch from source
    value = await fetch_func()

    # Store in cache
    await cache.set(key, value, ttl=ttl)

    return value
