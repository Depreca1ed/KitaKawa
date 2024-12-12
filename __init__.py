from __future__ import annotations

from typing import TYPE_CHECKING

from utils import BaseCog
if TYPE_CHECKING:
    from bot import DeBot
    from utils import DeContext

KITAKAWA_SERVER = 1277813689092804650

class KitaKawa(BaseCog, name='KitaKawa'):
    """For everything related Kitanai Kimi Ga Ichiban Kawaii's server"""

    @discord.utils.copy_doc(commands.Cog.cog_check)
    def cog_check(self, ctx: DeContext) -> bool:
        return bool(ctx.guild and ctx.guild.id == KITAKAWA_SERVER)

    

async def setup(bot: DeBot) -> None:
    await bot.add_cog(KitaKawa(bot))
