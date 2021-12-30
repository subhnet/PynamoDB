from typing import Generic, TYPE_CHECKING

GenericMeta = type if TYPE_CHECKING else type(Generic)
