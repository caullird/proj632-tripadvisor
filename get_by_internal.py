
import requests
import json

url = "https://api.tripadvisor.com/api/internal/1.0/graphql/?currency=EUR&lang=fr_FR"

payload = "{\"operationName\":\"HotelReview\",\"variables\":{\"locationId\":12414912,\"distanceUnit\":\"KILOMETERS\",\"language\":\"fr\",\"reviewFilters\":[{\"axis\":\"LANGUAGE\",\"selections\":[\"fr\"]}],\"reviewPrefsCacheKey\":\"hotelReviewPrefs_3968848\",\"reviewFilterCacheKey\":\"hotelReviewFilters_3968848\",\"geoIds\":[],\"socialPartialResults\":true,\"keywordVariant\":\"location_keywords_v2_llr_order_30_fr\"},\"query\":\"query HotelReview($locationId: Int!, $photoCount: Int = 20, $photoOffset: Int = 0, $distanceUnit: UnitLengthInput!, $language: String = \\\"en\\\", $roomTipsLimit: Int = 3, $roomTipsOffset: Int = 0, $reviewFilters: [FilterConditionInput!], $reviewPrefsCacheKey: String!, $reviewFilterCacheKey: String!, $geoIds: [Int!]!, $socialPartialResults: Boolean!, $keywordVariant: String!) {  locations(locationIds: [$locationId]) {    __typename    ...HotelReviewFields    ...HotelRoomTipsFields    ...HotelReviewSectionFields  }  notSortedtReviews: locations(locationIds: [$locationId]) {    __typename    ...HotelDetailsNotSortedReviews  }  coeAward(requests: [{ locations: [$locationId] }]) {    __typename    locations  }  travelersChoice(locationIds: [$locationId]) {    __typename    absoluteUrl    year    ranking  }  reviewContributions: connectionContributions(detailIds: [$locationId], geoIds: $geoIds, placeTypes: [ACCOMMODATION], connectionTypes: [ALL], contributionTypes: [REVIEW], includePartialResults: $socialPartialResults) {    __typename    ...POIConnectionReviewContributions  }  locationKeywords(locationIds: [$locationId], variant: $keywordVariant) {    __typename    keywords {      __typename      keyword      order    }  }}fragment HotelReviewFields on LocationInformation {  __typename  countryId  locationId  name  geoName  locationDescription  isGeo  locationTimezoneId  latitude  longitude  isClosed  thumbnail {    __typename    ...BasicPhotoInformation  }  parent {    __typename    locationId    name    isGeo    isBroadGeo  }  reviewSummary {    __typename    count    rating  }  photoCount  photos(filter: {mediaGroup: DEFAULT, mediaTypes: [PHOTO], supplierCategories: [OWNER, STAFF, TRAVELER]}, ordering: BIG_CAROUSEL, page: {limit: $photoCount, offset: $photoOffset}) {    __typename    id    photoSizes {      __typename      ... PhotoSizeFields    }  }  detail {    __typename    ... on Hotel {      styleRankings(max: 2) {        __typename        translatedName        score        geoRanking      }      hotel {        __typename        reviewSubratingAvgs {          __typename          avgRating          questionId          answerCount        }        numReviews        walkScore        greenLeader        providerStarRating      }      ...HotelStarRating      ...Amenities      ...NearbyLocations    }  }  streetAddress {    __typename    fullAddress  }  neighborhoods {    __typename    description  }  closeAirports: nearestAirports(limit: 2, radius: 500) {    __typename    distanceFromCenter    airportInfo {      __typename      locationName    }  }  nearbyTransit: nearby(radius: 1, page: {limit: 2, offset: 0}, locationFilter: {placeTypes: [METRO_STATION]}) {    __typename    locationId    name    distanceFromCenter    placeType  }}fragment HotelRoomTipsFields on LocationInformation {  __typename  roomTipsCount  roomTips(language: $language, page: {limit: $roomTipsLimit, offset: $roomTipsOffset}) {    __typename    id    rating    text    publishedDate    userId    userProfile {      __typename      ... HotelDetailsUserDetails    }  }}fragment HotelReviewSectionFields on LocationInformation {  __typename  reviewList(page: {limit: 5000, offset: 0}, initialPrefs: {sortType: \\\"connectionsFirst\\\", showMT: true}, prefs: {sortType: \\\"connectionsFirst\\\", showMT: true}, filters: $reviewFilters, prefsCacheKey: $reviewPrefsCacheKey, filterCacheKey: $reviewFilterCacheKey) {    __typename    languageCounts    preferredReviewIds    ratingCounts    totalCount    reviews {      __typename      ... HotelDetailsHotelReview    }  }}fragment BasicPhotoInformation on Photo {  __typename  photoId: id  locationId  caption  photoSizes {    __typename    ...PhotoSizeFields  }  photoRoute : route {    __typename    ...BasicPhotoDetailRoute  }}fragment PhotoSizeFields on PhotoSize {  __typename  height  url  width}fragment BasicPhotoDetailRoute on PhotoDetailRoute {  __typename  photoId  absoluteUrl}fragment HotelStarRating on Hotel {  __typename  starTags: tags(tagCategoryTypes: [STAR_RATING]) {    __typename    tagId    tagNameLocalized  }}fragment Amenities on Hotel {  __typename  amenityList: amenityList(prioritizeUserFilteredAmenities: true, showOnlyHighlightedAmenities: false) {    __typename    highlightedAmenities {      __typename      propertyAmenities {        __typename        amenityCategoryName        amenityIcon        amenityNameLocalized        tagId        translationKey      }      roomAmenities {        __typename        amenityCategoryName        amenityIcon        amenityNameLocalized        tagId        translationKey      }    }    nonHighlightedAmenities {      __typename      propertyAmenities {        __typename        amenityCategoryName        amenityIcon        amenityNameLocalized        tagId        translationKey      }      roomAmenities {        __typename        amenityCategoryName        amenityIcon        amenityNameLocalized        tagId        translationKey      }    }    languagesSpoken {      __typename      amenityCategoryName      amenityIcon      amenityNameLocalized      tagId      translationKey    }  }}fragment NearbyLocations on Hotel {  __typename  nearbyLocations(distanceUnit: $distanceUnit) {    __typename    attractionCount    distanceRange    distanceUnit    hotelCount    restaurantCount    locationList {      __typename      distanceFromCenter      locationId      placeType      location {        __typename        locationId        name        url        latitude        longitude        thumbnail {          __typename          id          photoSizes {            __typename            height            isHorizontal            url            width          }        }        reviewSummary {          __typename          count          rating        }        popIndexDetails {          __typename          popIndexRank          popIndexTotal        }        detail {          __typename          ... on Restaurant {            cuisines: tags(tagCategoryTypes: [CUISINES]) {              __typename              tagId              tagNameLocalized            }            priceRange: tags(tagCategoryTypes: [RESTAURANT_PRICE]) {              __typename              tagId              tag            }          }          ... on Attraction {            category: tags(tagCategoryTypes: [ATTRACTIONS_L2_CATEGORY]) {              __typename              tagId              tagNameLocalized            }            categoryType: tags(tagCategoryTypes: [ATTRACTIONS_L3_TYPE]) {              __typename              tagId              tagNameLocalized            }          }        }      }    }  }}fragment HotelDetailsUserDetails on MemberProfile {  __typename  avatar {    __typename    photoSizes {      __typename      ... PhotoSizeFields    }  }  displayName  username  isFollowing  isVerified  contributionCounts {    __typename    helpfulVote    sumAllUgc  }  hometown {    __typename    location {      __typename      additionalNames {        __typename        longParentAbbreviated      }    }  }}fragment HotelDetailsHotelReview on Review {  __typename  id  title  text  absoluteUrl  publishedDateTime  translationType  rating  helpfulVotes  language  originalLanguage  userId  additionalRatings {    __typename    rating    ratingLabel  }  tripInfo {    __typename    stayDate    tripType  }  socialStatistics {    __typename    isLiked    isReposted    isFollowing  }  photos {    __typename    caption    id    publishedDateTime    thumbsUpVotes    photoSizes {      __typename      ... PhotoSizeFields    }  }  ownerResponse {    __typename    text    publishedDateTime    username    connectionToSubject    language    originalLanguage    userProfile {      __typename      id      avatar {        __typename        photoSizes {          __typename          ... PhotoSizeFields        }      }    }  }  userProfile {    __typename    ... HotelDetailsUserDetails  }}fragment HotelDetailsNotSortedReviews on LocationInformation {  __typename  reviewList(page: {limit: 5, offset: 0}, initialPrefs: {sortType: \\\"\\\", showMT: true}, prefs: {sortType: \\\"\\\", showMT: true}, filters: $reviewFilters, prefsCacheKey: $reviewPrefsCacheKey, filterCacheKey: $reviewFilterCacheKey) {    __typename    preferredReviewIds    reviews {      __typename      ...HotelDetailsHotelReview    }  }}fragment POIConnectionReviewContributions on ConnectionContributionsResult {  __typename  status  contributionsByLocation {    __typename    locationId    userReviewContributions {      __typename      reviewId      rating      contributionReviewText {        __typename        text      }      userDisplayInformation {        __typename        userId        fullname        username        avatarUrl      }    }  }}\"}"
headers = {
  'X-TripAdvisor-Unique': '%1%enc%3A486P6PUqjuv2tSHEX3X6xWc%2FZ3NfeBAe1aAFFqx9nhin8H1B6ejIxA%3D%3D',
  'X-TripAdvisor-API-Key': 'ce957ab2-0385-40f2-a32d-ed80296ff67f',
  'Content-Type': 'application/json',
  'Cookie': 'ak_bmsc=8F5C7C1B582232E87263FF684F04B07E0216719C5F5400002E39186043341677~plHdq+a8eBKcpKy9oAIuj8rq9wopz2lSpWQHtsHD+JL8z744c8DLywjq6IK64wsE5azi6Q2saFFu+/nfkQQ6/QdY+lsXyJRlaqIKtCQ8HpnCPhXDhGLFS6Wnep0/38ImcOPWTV+m75Jw37Ozk2SeT4DMBPgS9+qZ2YJSlcF1D451z2eULum0rTZLKDJLAHWAo2tqLj+8S4r99y4Ymkztv6IlI26PsXh0EZjNGL8IiayLE=; __vt=ikfppl6QMa6UpP2iABQCaFWAfjiJQy2tOYzXavIgDBMYqsq8z8JqmQKEjRCoj6dWjxPrK2TpH9V-HHL6MaRt1BAgsc1Qt1m2M8XaRLLgWCHU9MOR-k1iG69nZAP4QoJ07QiXSJyzJdI4gbFvMuZZf3o; bm_sv=293DCF3BE1127ABDF999949BF53A1E4D~483CTSFuthKw3zLzqTfXFY2GeBHER9AP0fxY/W3C/cm/N1s0SoAXsmj7UssjnHj6/6z8p0J+YVgkWsUDBktKzuQ4BRHG3aoctn3wmnDOt8V0yNYUiiks/bSDJNW+QEsb6DSqVNQmef3jKlqC8TDe0WNjOJCdTkGcnxWlAQe6h2c='
}

response = requests.request("POST", url, headers=headers, data = payload)
response_json = response.json()
shearch = response_json['data']['locations'][0]['reviewList']['reviews']



for review in shearch:
	print(json.dumps(review['title'], indent = 4))

# print(response.text.encode('utf8'))
