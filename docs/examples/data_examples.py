from ipyvizzu import Data

music_example_data = Data()
music_example_data.add_dimension('Genres', [ 'Pop', 'Rock', 'Jazz', 'Metal'])
music_example_data.add_dimension('Types', [ 'Hard', 'Smooth', 'Experimental' ])
music_example_data.add_measure(
    'Popularity',
    [
        [114, 96, 78, 52],
        [56, 36, 174, 121],
        [127, 83, 94, 58],
    ]
)