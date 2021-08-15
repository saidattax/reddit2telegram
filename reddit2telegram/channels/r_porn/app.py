#encoding:utf-8

from utils import weighted_random_subreddit


subreddit = weighted_random_subreddit({
    'AbandonedPorn': 593,
    'AdPorn': 90,
    'AdrenalinePorn': 146,
    'AerialPorn': 20,
    'AgriculturePorn': 12,
    'AlbumArtPorn': 50,
    'AnimalPorn': 85,
    'ApocalypsePorn': 14,
    'ArchitecturePorn': 205,
    'ArtPorn': 177,
    'ArtefactPorn': 202,
    'AutumnPorn': 18,
    'Beachporn': 9,
    'BonsaiPorn': 9,
    'BotanicalPorn': 38,
    'CabinPorn': 59,
    'CemeteryPorn': 23,
    'CityPorn': 328,
    'ClimbingPorn': 22,
    'ComicBookPorn': 7,
    'ConcertPorn': 2,
    'CulinaryPorn': 18,
    'DesignPorn': 355,
    'DessertPorn': 46,
    'DestructionPorn': 58,
    'EarthPorn': 7000,
    'EarthlingPorn': 5,
    'ExposurePorn': 194,
    'F1Porn': 24,
    'FirePorn': 31,
    'FoodPorn': 868,
    'FossilPorn': 11,
    'FractalPorn': 24,
    'GamerPorn': 11,
    'GeekPorn': 34,
    'GunPorn': 81,
    'HellscapePorn': 9,
    'HistoryPorn': 894,
    'Houseporn': 54,
    'HumanPorn': 176,
    'InfraredPorn': 6,
    'InfrastructurePorn': 73,
    'InstrumentPorn': 17,
    'Knifeporn': 11,
    'MachinePorn': 189,
    'MacroPorn': 89,
    'MapPorn': 451,
    'MegalithPorn': 12,
    'MetalPorn': 11,
    'MicroPorn': 34,
    'MilitaryPorn': 173,
    'MotorcyclePorn': 17,
    'MoviePosterPorn': 96,
    'MushroomPorn': 8,
    'NewsPorn': 28,
    'OrganizationPorn': 22,
    'QuotesPorn': 200,
    'RetroGamePorn': 4,
    'RidesPorn': 5,
    'RoomPorn': 721,
    'SkyPorn': 65,
    'SportsPorn': 5,
    'SpringPorn': 5,
    'StarshipPorn': 21,
    'StreetArtPorn': 28,
    'SummerPorn': 5,
    'TeaPorn': 12,
    'TechnologyPorn': 22,
    'TelevisionPosterPorn': 6,
    'ThingsCutInHalfPorn': 234,
    'VideoPorn': 11,
    'ViewPorn': 10,
    'VillagePorn': 60,
    'WeatherPorn': 16,
    'avporn': 12,
    'boatporn': 15,
    'bookporn': 48,
    'bridgeporn': 7,
    'carporn': 362,
    'churchporn': 8,
    'desertporn': 6,
    'fashionporn': 14,
    'futureporn': 106,
    'geologyporn': 26,
    'lakeporn': 5,
    'lavaporn': 8,
    'mtgporn': 13,
    'policeporn': 15,
    'powerwashingporn': 301,
    'retailporn': 4,
    'ruralporn': 24,
    'seaporn': 20,
    'spaceflightporn': 10,
    'spaceporn': 543,
    'stadiumporn': 5,
    'steamporn': 4,
    'toolporn': 16,
    'uniformporn': 8,
    'waterporn': 73,
    'winterporn': 47
})
t_channel = '@r_porn'


def send_post(submission, r2t):
    limit_on_upvotes = {
        'AbandonedPorn': 1000,
        'AdPorn': 500,
        'AdrenalinePorn': 500,
        'AerialPorn': 50,
        'AgriculturePorn': 50,
        'AlbumArtPorn': 50,
        'AnimalPorn': 150,
        'ApocalypsePorn': 50,
        'ArchitecturePorn': 200,
        'ArtPorn': 150,
        'ArtefactPorn': 555,
        'AutumnPorn': 100,
        'Beachporn': 50,
        'BonsaiPorn': 100,
        'BotanicalPorn': 50,
        'CabinPorn': 555,
        'CemeteryPorn': 100,
        'CityPorn': 500,
        'ClimbingPorn': 100,
        'ComicBookPorn': 50,
        'ConcertPorn': 50,
        'CulinaryPorn': 50,
        'DesignPorn': 1000,
        'DessertPorn': 100,
        'DestructionPorn': 200,
        'EarthPorn': 3456,
        'EarthlingPorn': 50,
        'ExposurePorn': 200,
        'F1Porn': 100,
        'FirePorn': 100,
        'FoodPorn': 1234,
        'FossilPorn': 50,
        'FractalPorn': 50,
        'GamerPorn': 50,
        'GeekPorn': 100,
        'GunPorn': 300,
        'HellscapePorn': 100,
        'HistoryPorn': 2000,
        'Houseporn': 200,
        'HumanPorn': 314,
        'InfraredPorn': 50,
        'InfrastructurePorn': 256,
        'InstrumentPorn': 50,
        'Knifeporn': 50,
        'MachinePorn': 500,
        'MacroPorn': 128,
        'MapPorn': 300,
        'MegalithPorn': 100,
        'MetalPorn': 50,
        'MicroPorn': 200,
        'MilitaryPorn': 200,
        'MotorcyclePorn': 100,
        'MoviePosterPorn': 150,
        'MushroomPorn': 50,
        'NewsPorn': 100,
        'OrganizationPorn': 200,
        'QuotesPorn': 987,
        'RetroGamePorn': 50,
        'RidesPorn': 50,
        'RoomPorn': 1600,
        'SkyPorn': 100,
        'SportsPorn': 50,
        'SpringPorn': 50,
        'StarshipPorn': 150,
        'StreetArtPorn': 100,
        'SummerPorn': 50,
        'TeaPorn': 50,
        'TechnologyPorn': 100,
        'TelevisionPosterPorn': 50,
        'ThingsCutInHalfPorn': 666,
        'VideoPorn': 50,
        'ViewPorn': 50,
        'VillagePorn': 200,
        'WeatherPorn': 100,
        'avporn': 50,
        'boatporn': 50,
        'bookporn': 100,
        'bridgeporn': 50,
        'carporn': 666,
        'churchporn': 50,
        'desertporn': 50,
        'fashionporn': 100,
        'futureporn': 555,
        'geologyporn': 100,
        'lakeporn': 50,
        'lavaporn': 66,
        'mtgporn': 100,
        'policeporn': 150,
        'powerwashingporn': 1248,
        'retailporn': 50,
        'ruralporn': 50,
        'seaporn': 100,
        'spaceflightporn': 100,
        'spaceporn': 1000,
        'stadiumporn': 50,
        'steamporn': 50,
        'toolporn': 100,
        'uniformporn': 100,
        'waterporn': 127,
        'winterporn': 150
    }

    return r2t.send_simple(submission,
        check_dups=True,
        min_upvotes_limit=limit_on_upvotes[subreddit],
        text='{title}\n\n{self_text}\n\n{upvotes} upvotes\n/r/{subreddit_name} → #{subreddit_name}\n{short_link}\n{channel}',
        other='{title}\n{link}\n\n{upvotes} upvotes\n/r/{subreddit_name} → #{subreddit_name}\n{short_link}\n{channel}',
        album='{title}\n{link}\n\n{upvotes} upvotes\n/r/{subreddit_name} → #{subreddit_name}\n{short_link}\n{channel}',
        gif='{title}\n\n{upvotes} upvotes\n/r/{subreddit_name} → #{subreddit_name}\n{short_link}\n{channel}',
        img='{title}\n\n{upvotes} upvotes\n/r/{subreddit_name} → #{subreddit_name}\n{short_link}\n{channel}',
        video='{title}\n\n{upvotes} upvotes\n/r/{subreddit_name} → #{subreddit_name}\n{short_link}\n{channel}',
        gallery='{title}\n\n{upvotes} upvotes\n/r/{subreddit_name} → #{subreddit_name}\n{short_link}\n{channel}'
    )
