from dataclasses import dataclass, field
from typing import List

import dataclass_factory
from dataclass_factory import NameStyle, Schema


@dataclass
class UniqueMovie:
    title: str = ""
    year: str = ""
    rated: str = ""
    released: str = ""
    runtime: str = ""
    genre: str = ""
    director: str = ""
    writer: str = ""
    actors: str = ""
    plot: str = ""
    language: str = ""
    country: str = ""
    awards: str = ""
    poster: str = ""
    metascore: str = ""
    imdb_rating: str = ""
    imdb_votes: str = ""
    imdb_id: str = ""
    type: str = ""
    total_seasons: str = ""
    response: str = ""


@dataclass
class Movies:
    movies_list: List[UniqueMovie] = field(default_factory=list)


mapping_factory = dataclass_factory.Factory(schemas={UniqueMovie: Schema(
    name_mapping={"imdb_rating": "imdbRating", "imdb_votes": "imdbVotes", "imdb_id": "imdbID",
                  "total_seasons": "totalSeasons"}, name_style=NameStyle.camel)})
