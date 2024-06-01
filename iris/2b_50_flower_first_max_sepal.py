with open (file ="../../../../Bai_Tap_Buoi_2/Iris.csv", mode ="r") as file:
    sum_sepal_iris = []
    top_50_max_sepal = []
    value_sum_sepal_iris = []
    species_sepal_iris = []
    for line in file:
        line = line.split(",")
        if line[5] == 'Iris-setosa\n' or line[5] ==  'Iris-versicolor\n' or line[5] == 'Iris-virginica\n':
            temp_array = [line[5], float(line[1]) + float(line[2])]
            sum_sepal_iris.append(temp_array)
    for i in sum_sepal_iris:
        species_sepal_iris.append(i[0])
        value_sum_sepal_iris.append(i[1])
    sort_value_sum_sepal_iris =sorted(value_sum_sepal_iris,reverse=True)[:50]

    index_top_50_sum_sepal = []
    for i in range(50):
         index_top_50_sum_sepal.append(value_sum_sepal_iris.index(sort_value_sum_sepal_iris[i]))

    for i in index_top_50_sum_sepal:
        top_50_max_sepal.append(sum_sepal_iris[i])

    print(top_50_max_sepal)

    