from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from accessors import LiChessAccessor
from processors import LiChessProcessor


class Container(containers.DeclarativeContainer):
    lichess_accessor = providers.Singleton(LiChessAccessor.LiChessAccessor)
    lichess_processor = providers.Factory(
        LiChessProcessor.LiChessProcessor, lichess_accessor=lichess_accessor
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
