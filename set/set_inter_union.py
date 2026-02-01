#intersection and union of two sets
#intersection is common b/w two sets
#union is all elements from both sets without duplicates

fri_circle1 = {"Ajeet","Scachin","Shiv","Arshit"}
fri_circle2 = {"Ajeet","Scachin","Anuraj","Rohit"}

#intersection
common_fri = fri_circle1.intersection(fri_circle2)
print(f"Common friends: {common_fri}")
#another way to find intersection
common_fri2 = fri_circle1 & fri_circle2
print(f"Common friends (using &): {common_fri2}")

#union
all_fri = fri_circle1.union(fri_circle2)
print(f"All friends: {all_fri}")

#difference (b/w two sets)
#difference b/w fri_circle1 and fri_circle2
unique_fri1 = fri_circle1.difference(fri_circle2)
print(f"Friends only in circle 1: {unique_fri1}")
#difference b/w fri_circle2 and fri_circle1 