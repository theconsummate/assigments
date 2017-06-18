library(dplyr)
diabetes <- read.csv("diabetes.csv")

# the last 16 lines are  NA
diabetes <- diabetes %>% filter(!is.na(id))

# create variables for BMI and WHR
diabetes <- diabetes %>% mutate(BMI = 703*weight/(height^2))
diabetes <- diabetes %>% mutate(WHR = waist/hip)

diabetes <- diabetes %>% mutate(BMI.standards = cut(BMI, breaks = c(16,18.5, 25, 30, 35, 40, 60)))
levels(diabetes$BMI.standards)  <- c("Underweight", "Healthy", "Overweight", "Level 1 Obese", "Level 2 Obese", "Level 3 Obese")




# create a variable for the age interval
diabetes <- diabetes %>% mutate(age.intervals = cut(age, breaks = c(18, 30, 40, 50, 60, 100)))

# generate categories for males in their 20s
diab.male.20s <- diabetes %>% 
  filter(age < 30 & age >= 19 & gender == "male") %>%
  mutate(WHR.standards = cut(WHR, breaks = c(0.6, 0.83, 0.88, 0.94, 1.2)))
levels(diab.male.20s$WHR.standards) <- c("Low","Moderate","High", "Very High")

# generate categories for males in their 30s
diab.male.30s <- diabetes %>% 
  filter(age < 40 & age >= 30 & gender == "male") %>%
  mutate(WHR.standards = cut(WHR, breaks = c(0.6, 0.84, 0.91, 0.96, 1.2)))
levels(diab.male.30s$WHR.standards) <- c("Low","Moderate","High", "Very High")

# generate categories for males in their 40s
diab.male.40s <- diabetes %>% 
  filter(age < 50 & age >= 40 & gender == "male") %>%
  mutate(WHR.standards = cut(WHR, breaks = c(0.6, 0.88, 0.95, 1.0, 1.2)))
levels(diab.male.40s$WHR.standards) <- c("Low","Moderate","High", "Very High")


# generate categories for males in their 50s
diab.male.50s <- diabetes %>% 
  filter(age < 60 & age >= 50 & gender == "male") %>%
  mutate(WHR.standards = cut(WHR, breaks = c(0.6, 0.90, 0.97, 1.02, 1.2)))
levels(diab.male.50s$WHR.standards) <- c("Low","Moderate","High", "Very High")


# generate categories for males in their 60s
diab.male.60s <- diabetes %>% 
  filter(age < 100 & age >= 60 & gender == "male") %>%
  mutate(WHR.standards = cut(WHR, breaks = c(0.6, 0.91, 0.98, 1.03, 1.2)))
levels(diab.male.60s$WHR.standards) <- c("Low","Moderate","High", "Very High")




# generate categories for females in their 20s
diab.female.20s <- diabetes %>% 
  filter(age < 30 & age >= 19 & gender == "female") %>%
  mutate(WHR.standards = cut(WHR, breaks = c(0.6, 0.71, 0.77, 0.82, 1.2)))
levels(diab.female.20s$WHR.standards) <- c("Low","Moderate","High", "Very High")

# generate categories for females in their 30s
diab.female.30s <- diabetes %>% 
  filter(age < 40 & age >= 30 & gender == "female") %>%
  mutate(WHR.standards = cut(WHR, breaks = c(0.6, 0.72, 0.78, 0.84, 1.2)))
levels(diab.female.30s$WHR.standards) <- c("Low","Moderate","High", "Very High")

# generate categories for females in their 40s
diab.female.40s <- diabetes %>% 
  filter(age < 50 & age >= 40 & gender == "female") %>%
  mutate(WHR.standards = cut(WHR, breaks = c(0.6, 0.73, 0.79, 87, 1.2)))
levels(diab.female.40s$WHR.standards) <- c("Low","Moderate","High", "Very High")


# generate categories for females in their 50s
diab.female.50s <- diabetes %>% 
  filter(age < 60 & age >= 50 & gender == "female") %>%
  mutate(WHR.standards = cut(WHR, breaks = c(0.6, 0.74, 0.81, 0.88, 1.2)))
levels(diab.female.50s$WHR.standards) <- c("Low","Moderate","High", "Very High")


# generate categories for females in their 60s
diab.female.60s <- diabetes %>% 
  filter(age < 100 & age >= 60 & gender == "female") %>%
  mutate(WHR.standards = cut(WHR, breaks = c(0.6, 0.76, 0.83, 0.9, 1.2)))
levels(diab.female.60s$WHR.standards) <- c("Low","Moderate","High", "Very High")

# join these dataset
diabetes2 <- rbind(diab.female.60s, diab.female.50s, diab.female.40s, diab.female.30s, diab.female.20s, diab.male.60s, diab.male.50s, diab.male.40s, diab.male.30s, diab.male.20s)
# rearrange dataset so that rows are in the same order as the original dataset
diabetes2 <- diabetes2 %>% arrange(id)
