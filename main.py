import sys
import logging
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from accessors import LiChessAccessor
from processors import LiChessProcessor


class Container(containers.DeclarativeContainer):
    logger = logging.getLogger("stock_pepper_dog")
    logger.setLevel(logging.WARNING)
    file_handler = logging.FileHandler("stock_pepper_dog.log")
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s : %(name)s  : %(funcName)s : %(levelname)s : %(message)s"
    )

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    lichess_accessor = providers.Singleton(LiChessAccessor.LiChessAccessor)
    lichess_processor = providers.Factory(
        LiChessProcessor.LiChessProcessor,
        lichess_accessor=lichess_accessor,
        logger=logger,
    )


@inject
def main(
    service: LiChessProcessor.LiChessProcessor = Provide[Container.lichess_processor],
) -> None:
    service.start()


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    main()
