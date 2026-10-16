from .blocksworld import BlocksWorldTranslator
from .depot import DepotTranslator
from .ferry import FerryTranslator
from .floortile import FloorTileTranslator
from .goldminer import GoldMinerTranslator
from .grid import GridTranslator
from .grippers import GrippersTranslator
from .logistics import LogisticsTranslator
from .rovers import RoversTranslator
from .satellite import SatelliteTranslator
from .swap import SwapTranslator
from .visitall import VisitallTranslator
from .alfworld import AlfworldTranslator
from .hanoi import HanoiTranslator, RandomHanoiTranslator
from .frogs_jumping import FrogsJumpingTranslator

def get_translator(domain):
    if domain == "blocksworld":
        return BlocksWorldTranslator
    elif domain == "depot":
        return  DepotTranslator
    elif domain == "ferry":
        return  FerryTranslator
    elif domain == "floortile":
        return  FloorTileTranslator
    elif domain == "goldminer":
        return  GoldMinerTranslator
    elif domain == "grid":
        return  GridTranslator
    elif domain == "grippers":
        return  GrippersTranslator
    elif domain == "logistics":
        return  LogisticsTranslator
    elif domain == "rovers":
        return  RoversTranslator
    elif domain == "satellite":
        return  SatelliteTranslator
    elif domain == "swap":
        return SwapTranslator
    elif domain == "visitall":
        return  VisitallTranslator
    elif domain == "alfworld":
        return AlfworldTranslator
    elif domain == "hanoi":
        return HanoiTranslator
    elif domain== "random_hanoi":
        return RandomHanoiTranslator
    elif domain== "frogs_jumping":
        return FrogsJumpingTranslator