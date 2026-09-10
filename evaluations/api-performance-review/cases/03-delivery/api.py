"""Disposable provider fake with explicit ambiguous-completion semantics."""
import asyncio


class Provider:
    def __init__(self):
        self.effects = []

    async def deliver(self, order_id):
        self.effects.append(order_id)
        # The remote effect committed; the response is lost on the first call.
        if len(self.effects) == 1:
            raise TimeoutError("response lost after commit")
        return "delivered"


async def deliver_order(provider, order_id):
    for attempt in range(3):
        try:
            return await provider.deliver(order_id)
        except TimeoutError:
            if attempt == 2:
                raise
            await asyncio.sleep(0)
