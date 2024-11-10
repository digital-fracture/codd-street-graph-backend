from uuid import UUID

from fastapi import UploadFile

from data import schemas, crud
from misc.util import save_to_storage

_history = schemas.GraphHistory(
    graphs=[
        schemas.StreetGraphPair(
            nodes=[
                schemas.StreetGraphNode(
                    id=1,
                    name="1",
                    position=(55.664454, 37.773391),
                    connections=[
                        schemas.StreetGraphEdge(id=2, width=1, flow=100, load_percentage=12.5),
                        schemas.StreetGraphEdge(id=4, width=1, flow=50, load_percentage=6.25),
                    ],
                ),
                schemas.StreetGraphNode(
                    id=2,
                    name="2",
                    position=(55.664125, 37.772483),
                    connections=[
                        schemas.StreetGraphEdge(id=5, width=1, flow=50, load_percentage=6.25)
                    ],
                ),
                schemas.StreetGraphNode(
                    id=3,
                    name="3",
                    position=(55.664277, 37.773626),
                    connections=[
                        schemas.StreetGraphEdge(id=4, width=2, flow=400, load_percentage=50.0),
                        schemas.StreetGraphEdge(id=6, width=2, flow=250, load_percentage=31.25),
                    ],
                ),
                schemas.StreetGraphNode(
                    id=4,
                    name="4",
                    position=(55.663935, 37.772695),
                    connections=[
                        schemas.StreetGraphEdge(id=5, width=2, flow=400, load_percentage=50.0)
                    ],
                ),
                schemas.StreetGraphNode(
                    id=5,
                    name="5",
                    position=(55.663644, 37.771919),
                    connections=[
                        schemas.StreetGraphEdge(id=8, width=3, flow=550, load_percentage=68.75)
                    ],
                ),
                schemas.StreetGraphNode(
                    id=6,
                    name="6",
                    position=(55.664055, 37.773859),
                    connections=[
                        schemas.StreetGraphEdge(id=7, width=1, flow=150, load_percentage=18.75)
                    ],
                ),
                schemas.StreetGraphNode(
                    id=7,
                    name="7",
                    position=(55.663695, 37.772991),
                    connections=[
                        schemas.StreetGraphEdge(id=8, width=1, flow=150, load_percentage=18.75)
                    ],
                ),
                schemas.StreetGraphNode(
                    id=8, name="8", position=(55.66337, 37.772252), connections=[]
                ),
                schemas.StreetGraphNode(
                    id=9,
                    name="9",
                    position=(55.663947, 37.771542),
                    connections=[
                        schemas.StreetGraphEdge(id=5, width=3, flow=500, load_percentage=62.5)
                    ],
                ),
            ],
            buildings=[
                [
                    (55.664611, 37.773094),
                    (55.664456, 37.773287),
                    (55.664162, 37.772487),
                    (55.664293, 37.772348),
                ],
                [
                    (55.66422, 37.773593),
                    (55.664092, 37.773759),
                    (55.663795, 37.773051),
                    (55.663929, 37.772847),
                ],
                [
                    (55.664378, 37.772053),
                    (55.664099, 37.772058),
                    (55.66409, 37.771688),
                    (55.664366, 37.771704),
                ],
                [
                    (55.663486, 37.773094),
                    (55.663225, 37.773083),
                    (55.663219, 37.772718),
                    (55.663489, 37.772734),
                ],
                [
                    (55.66389, 37.773947),
                    (55.662819, 37.775234),
                    (55.662731, 37.774993),
                    (55.663705, 37.77385),
                    (55.663541, 37.773416),
                    (55.663671, 37.773281),
                ],
            ],
            year=2023,
            update_nodes=[
                schemas.StreetGraphNode(
                    id=1,
                    name="1",
                    position=(55.664454, 37.773391),
                    connections=[
                        schemas.StreetGraphEdge(id=2, width=1, flow=100, load_percentage=12.5),
                        schemas.StreetGraphEdge(id=4, width=1, flow=50, load_percentage=6.25),
                    ],
                ),
                schemas.StreetGraphNode(
                    id=2,
                    name="2",
                    position=(55.664125, 37.772483),
                    connections=[
                        schemas.StreetGraphEdge(id=5, width=1, flow=50, load_percentage=6.25)
                    ],
                ),
                schemas.StreetGraphNode(
                    id=3,
                    name="3",
                    position=(55.664277, 37.773626),
                    connections=[
                        schemas.StreetGraphEdge(id=4, width=2, flow=400, load_percentage=50.0),
                        schemas.StreetGraphEdge(id=6, width=2, flow=250, load_percentage=31.25),
                    ],
                ),
                schemas.StreetGraphNode(
                    id=4,
                    name="4",
                    position=(55.663935, 37.772695),
                    connections=[
                        schemas.StreetGraphEdge(id=5, width=2, flow=400, load_percentage=50.0)
                    ],
                ),
                schemas.StreetGraphNode(
                    id=5,
                    name="5",
                    position=(55.663644, 37.771919),
                    connections=[
                        schemas.StreetGraphEdge(id=8, width=3, flow=550, load_percentage=68.75)
                    ],
                ),
                schemas.StreetGraphNode(
                    id=6,
                    name="6",
                    position=(55.664055, 37.773859),
                    connections=[
                        schemas.StreetGraphEdge(id=7, width=1, flow=150, load_percentage=18.75)
                    ],
                ),
                schemas.StreetGraphNode(
                    id=7,
                    name="7",
                    position=(55.663695, 37.772991),
                    connections=[
                        schemas.StreetGraphEdge(id=8, width=1, flow=150, load_percentage=18.75)
                    ],
                ),
                schemas.StreetGraphNode(
                    id=8, name="8", position=(55.66337, 37.772252), connections=[]
                ),
                schemas.StreetGraphNode(
                    id=9,
                    name="9",
                    position=(55.663947, 37.771542),
                    connections=[
                        schemas.StreetGraphEdge(id=5, width=3, flow=500, load_percentage=62.5)
                    ],
                ),
            ],
            hot_points=[
                (55.663644, 37.771919),
                (55.663947, 37.771542),
            ],
        ),
        schemas.StreetGraphPair(
            nodes=[
                schemas.StreetGraphNode(
                    id=1,
                    name="1",
                    position=(55.664454, 37.773391),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=2, width=1, flow=100, load_percentage=12.5, year=2023
                        ),
                        schemas.StreetGraphEdge(
                            id=3, width=2, flow=250, load_percentage=31.25, year=2023
                        ),
                    ],
                ),
                schemas.StreetGraphNode(
                    id=2,
                    name="2",
                    position=(55.664125, 37.772483),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=4, width=2, flow=300, load_percentage=37.5, year=2023
                        )
                    ],
                ),
                schemas.StreetGraphNode(
                    id=3,
                    name="3",
                    position=(55.664277, 37.773626),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=4, width=2, flow=300, load_percentage=37.5, year=2023
                        ),
                        schemas.StreetGraphEdge(
                            id=6, width=2, flow=250, load_percentage=31.25, year=2023
                        ),
                    ],
                ),
                schemas.StreetGraphNode(
                    id=4,
                    name="4",
                    position=(55.663935, 37.772695),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=5, width=2, flow=300, load_percentage=37.5, year=2023
                        ),
                        schemas.StreetGraphEdge(
                            id=7, width=2, flow=400, load_percentage=50.0, year=2023
                        ),
                    ],
                ),
                schemas.StreetGraphNode(
                    id=5,
                    name="5",
                    position=(55.663644, 37.771919),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=9, width=3, flow=500, load_percentage=62.5, year=2023
                        )
                    ],
                ),
                schemas.StreetGraphNode(
                    id=6,
                    name="6",
                    position=(55.664055, 37.773859),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=7, width=1, flow=150, load_percentage=18.75, year=2023
                        )
                    ],
                ),
                schemas.StreetGraphNode(
                    id=7,
                    name="7",
                    position=(55.663695, 37.772991),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=8, width=1, flow=150, load_percentage=18.75, year=2023
                        )
                    ],
                ),
                schemas.StreetGraphNode(
                    id=8,
                    name="8",
                    position=(55.66337, 37.772252),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=5, width=3, flow=500, load_percentage=62.5, year=2023
                        )
                    ],
                ),
                schemas.StreetGraphNode(
                    id=9, name="9", position=(55.663947, 37.771542), connections=[]
                ),
            ],
            buildings=[
                [
                    (55.664611, 37.773094),
                    (55.664456, 37.773287),
                    (55.664162, 37.772487),
                    (55.664293, 37.772348),
                ],
                [
                    (55.66422, 37.773593),
                    (55.664092, 37.773759),
                    (55.663795, 37.773051),
                    (55.663929, 37.772847),
                ],
                [
                    (55.664378, 37.772053),
                    (55.664099, 37.772058),
                    (55.66409, 37.771688),
                    (55.664366, 37.771704),
                ],
                [
                    (55.663486, 37.773094),
                    (55.663225, 37.773083),
                    (55.663219, 37.772718),
                    (55.663489, 37.772734),
                ],
                [
                    (55.66389, 37.773947),
                    (55.662819, 37.775234),
                    (55.662731, 37.774993),
                    (55.663705, 37.77385),
                    (55.663541, 37.773416),
                    (55.663671, 37.773281),
                ],
            ],
            year=2024,
            update_nodes=[
                schemas.StreetGraphNode(
                    id=1,
                    name="1",
                    position=(55.664454, 37.773391),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=2, width=1, flow=100, load_percentage=12.5, year=2023
                        ),
                        schemas.StreetGraphEdge(
                            id=3, width=2, flow=250, load_percentage=31.25, year=2023
                        ),
                    ],
                ),
                schemas.StreetGraphNode(
                    id=2,
                    name="2",
                    position=(55.664125, 37.772483),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=4, width=2, flow=300, load_percentage=37.5, year=2023
                        )
                    ],
                ),
                schemas.StreetGraphNode(
                    id=3,
                    name="3",
                    position=(55.664277, 37.773626),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=4, width=2, flow=300, load_percentage=37.5, year=2023
                        ),
                        schemas.StreetGraphEdge(
                            id=6, width=2, flow=250, load_percentage=31.25, year=2023
                        ),
                    ],
                ),
                schemas.StreetGraphNode(
                    id=4,
                    name="4",
                    position=(55.663935, 37.772695),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=5, width=2, flow=300, load_percentage=37.5, year=2023
                        ),
                        schemas.StreetGraphEdge(
                            id=7, width=2, flow=400, load_percentage=50.0, year=2023
                        ),
                    ],
                ),
                schemas.StreetGraphNode(
                    id=5,
                    name="5",
                    position=(55.663644, 37.771919),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=9, width=3, flow=500, load_percentage=62.5, year=2023
                        )
                    ],
                ),
                schemas.StreetGraphNode(
                    id=6,
                    name="6",
                    position=(55.664055, 37.773859),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=7, width=1, flow=150, load_percentage=18.75, year=2023
                        )
                    ],
                ),
                schemas.StreetGraphNode(
                    id=7,
                    name="7",
                    position=(55.663695, 37.772991),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=8, width=1, flow=150, load_percentage=18.75, year=2023
                        )
                    ],
                ),
                schemas.StreetGraphNode(
                    id=8,
                    name="8",
                    position=(55.66337, 37.772252),
                    connections=[
                        schemas.StreetGraphEdge(
                            id=5, width=3, flow=500, load_percentage=62.5, year=2023
                        )
                    ],
                ),
                schemas.StreetGraphNode(
                    id=9, name="9", position=(55.663947, 37.771542), connections=[]
                ),
            ],
            hot_points=[
                (55.663644, 37.771919),
                (55.663947, 37.771542),
            ],
        ),
    ],
)

_buildings = [
    [
        (55.664611, 37.773094),
        (55.664456, 37.773287),
        (55.664162, 37.772487),
        (55.664293, 37.772348),
    ],
    [
        (55.664220, 37.773593),
        (55.664092, 37.773759),
        (55.663795, 37.773051),
        (55.663929, 37.772847),
    ],
    [
        (55.664378, 37.772053),
        (55.664099, 37.772058),
        (55.664090, 37.771688),
        (55.664366, 37.771704),
    ],
    [
        (55.663486, 37.773094),
        (55.663225, 37.773083),
        (55.663219, 37.772718),
        (55.663489, 37.772734),
    ],
    [
        (55.663890, 37.773947),
        (55.662819, 37.775234),
        (55.662731, 37.774993),
        (55.663705, 37.773850),
        (55.663541, 37.773416),
        (55.663671, 37.773281),
    ],
]


async def handle_upload(file: UploadFile, user_id: UUID, year: int) -> schemas.StreetGraphPair:
    path = await save_to_storage(file)

    graph_pair = schemas.StreetGraphPair(
        nodes=_history.graphs[0].nodes,
        update_nodes=_history.graphs[0].update_nodes,
        hot_points=_history.graphs[0].hot_points,
        buildings=_buildings,
        year=year,
    )

    await crud.create_upload(user_id, year, path, graph_pair)

    return graph_pair


async def handle_regenerate(
    user_id: UUID, year: int, parameters: schemas.PopulationDistribution
) -> schemas.StreetGraph:
    return schemas.StreetGraph(
        nodes=_history.graphs[1].update_nodes,
        hot_points=_history.graphs[1].hot_points,
        buildings=_buildings,
        year=year,
    )
