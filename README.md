# 🌱 Plant Loving Score (PLS)
The project combines numerical, binary, and categorical variables into a weighted **0–100 PLS**, then compares different regression algorithms for learning the resulting score.
The PLS is based on four primary features:
- `plant_number`
- `plant_diversity`
- `rare_exotic`
- `plant_type`
  
These features are converted into component scores and combined using predetermined weights.
---
## 📊 Dataset Variables

| Variable | Description | Type |
|---|---|---|
| `plant_number` | Total number of plants | Numerical |
| `plant_diversity` | Number of distinct plant varieties/species | Numerical |
| `rare_exotic` | Presence of a rare/exotic plant | Binary |
| `plant_type` | Plant type category | Categorical |
| `PNS` | Plant Number Score | Continuous |
| `PDS` | Plant Diversity Score | Continuous |
| `RES` | Rare/Exotic Score | Continuous |
| `PTS` | Plant Type Score | Continuous |
| `PLS` | Final Plant Loving Score | Interval |
| `PLS_category` | Categorized PLS | Ordered categorical |

---
## 🌿 Plant Number
`plant_number` ranges from **1 to 100**.
The Plant Number Score (PNS) follows an **inverted-U relationship**:
- Increases from 1 to 20 plants
- Reaches a maximum of 100 at 20 plants
- Gradually decreases from 20 to 100 plants
---
## 🌱 Plant Diversity
`plant_diversity` represents the number of distinct plant varieties/species.
The Plant Diversity Score (PDS) also follows an **inverted-U relationship**:

- Increases from 1 to 10
- Reaches 100 at 10
- Gradually decreases toward 0 from 10 to 100
---
## 🪴 Rare/Exotic Plant
`rare_exotic` is a binary variable:
- `0` = absence
- `1` = presence

## 🌵 Plant Type

`plant_type` contains six predefined categories:

| Code | Type |
|---:|---|
| 0 | Flowering |
| 1 | Foliage |
| 2 | Fern |
| 3 | Succulent |
| 4 | Bonsai |
| 5 | Cacti |
