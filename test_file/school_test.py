import random, math, copy
country_x, country_y, number = [], [], []
max_fitness = 2000 #최대 적합도 설정
random_country = [] #초기 유전자 세대
cost = [] #비용
score_list = [] #적합도 함수
selection_list = []
random_country_2 = [] #선택 유전자

#위치의 범위 -100 < (x,y) < 100
def generate_country(length): #도시 생성
    for i in range(length):
        country_x.append(random.randint(-5, 5))
        country_y.append(random.randint(-5, 5))

        ##print(i+1,'번 도시 :' ,'(' , country_x[i], ',', country_y[i], ')')
        
        number.append(i+1)
        
    #print(country_x, country_y)
    
    return country_x, country_y, number
   
#도시 사이 거리 구하는 함수 
def value(num):
    for i in range(num):
        a = []
        for j in range(num):
            length = math.sqrt((country_x[i]-country_x[j])**2 + (country_y[i]-country_y[j])**2)
            r_length = round(length)
            a.append(r_length)
        cost.append(a)
    
    #print(cost)
    
    return cost

#초기 유전자 생성
def first_generation(num):
    a, b = 0, 0 

    while a != 1:
        list_A = [] #리스트 초기화
        while b != 1:
            i = random.randrange(1 ,num + 1) #num까지의 정수 생성
            if i not in list_A:
                list_A.append(i)
            if len(list_A) == num:
                b = 1
                #print(list_A)
        random_country.append(list_A)
        b = 0
        if len(random_country) == num:
            a = 1
    
    print('random_country :',random_country)
    
    return random_country

#적합도 함수
def sum_value(num):
    for i in random_country:
        fitness, score = [], 0
        for j in range(len(i)):
            a = number.index(i[j])
            fitness.append(a)
        #print(fitness)
        for j in range(num - 1):
            #print(fitness[j], fitness[j+1])
            a = cost[fitness[j]][fitness[j+1]]
            score = score + a
        score_list.append(score)
    ##print('적합도 함수 :', score_list)
        
    return score_list

#적합도 함수_2
def sum_value_2(num, random_country = []):
    
    score_list = []
    print(f"test{test}")
    
    print('적합도 안 random_country \n', random_country)
    
    for i in random_country:
        fitness, score = [], 0
        for j in range(len(i)):
            a = number.index(i[j])
            fitness.append(a)
        #print(fitness)
        for j in range(num - 1):
            #print(fitness[j], fitness[j+1])
            a = cost[fitness[j]][fitness[j+1]]
            score = score + a
        score_list.append(score)
    ##print('적합도 함수 :', score_list)
        
    return score_list

#유전자 선택(룰렛 휠 방식)
def selection(num):
    
    ##print('반환된 적합도 : ', score_list)
    
    x_sum, selection_list, random_country_2 = 0, [], []
    
    for i in score_list:
        x_sum = x_sum + i
    
    #print('x-sum :', x_sum)
    
    for i in score_list:
        value = i / x_sum
        selection_list.append(round(value, 2))
        
    ##print('적합도 : ', selection_list)
    ##print('가중치, 숫자 : ', tuple(selection_list), ',', number)
    
    a = random.choices(number, weights = tuple(selection_list), k = 2)
    
    ##print('a 값 : ', a)
    
    for i in a:
        #print(random_country)

        random_country_2.append(random_country[i-1])
        
    #print('random_country_2 :', random_country_2)
    
    parents_1 = random_country_2[0]
    parents_2 = random_country_2[1]

    ##print('parents :', parents_1, parents_2)
    
    return parents_1, parents_2


#교배(Crossover) & 돌연변이
def crossover_mutation(gene, mutation_rate):
    a, gene = 0, list(gene)
    ##print('부모유전자 :' , gene)
    
    mid_value = round(len(gene[0])/2)
    
    #while a != 1:
    for a in range(1):
        Mutation_list = []
        A_list = gene[0][:mid_value]
        B_list = gene[1][mid_value:]
        
        #print('자른 유전자 :' ,A_list, B_list)
        
        #Crossover(교배)
        while len(A_list) != GA_TSP:
            for i in B_list:
                if i not in A_list:
                    A_list.append(i)
            if len(A_list) != GA_TSP:
                for j in number:
                    if j not in A_list:
                        A_list.append(j)
            if len(A_list) == GA_TSP:
                continue
            print(A_list)
        
        select_list = [0, 1]
        #돌연변이 선택
        mutation_select = random.choices(select_list, weights = (1-mutation_rate, mutation_rate))
        
        #print('돌연변이 선택 1 :',mutation_select)
        #Mutation(돌연변이)
        if mutation_select == [1]:
            a = random.randrange(0, GA_TSP-4)
            b = random.randrange(0, GA_TSP)
            
            while (b < a) or (b == a) :
                b = random.randrange(0, GA_TSP)
            mutation = random.choices([1, 2], weights = (50, 50))
            #Swap Mutation
            #print('돌연변이 선택 2 :',mutation, 'A, B 값 :' ,a, b)
            
            if mutation == [1]:
                old_value = A_list[a]
                #print('예전 값', old_value)
                A_list[a] = A_list[b]
                A_list[b] = old_value
                #print('돌연변이 1 :', A_list)
            else:
                B_list, C_list = A_list[a:b], []
                for i in B_list[: : -1]:
                    C_list.append(i)
                #print('리스트 A :', A_list)
                #print('리스트 B :', B_list)
                #print('리스트 C :', C_list)
                del A_list[a:b]
                #print('자른 A :',A_list)
                for i in B_list:
                    A_list.insert(a, i)
                #print('돌연변이 2 :',A_list)
        
        #print(B_list, A_list)
        
    baby_gene = A_list

    print("자식 유전자 :",baby_gene)
    
    return baby_gene

#적합도 평가
def fitness():
    for i in score_list:
        sum_fitness = max_fitness - i
        
    return sum_fitness

GA_TSP = int(input('도시의 개수를 입력해주세요 :'))

def play(times):
    generate_country(GA_TSP) #GA_TSP 만큼의 도시 생성
    value(GA_TSP) #도시 사이의 거리 비용 구하는 함수 (cost 값 반환)
    first_generation(GA_TSP) #초기 유전자 세대 생성 (random_country 값 반환)
    sum_value(GA_TSP) #세대 적합도 구하는 함수 (score_list 값 반환)
    for i in range(times):
        #선택한 부모 유전자를 바탕으로 교배 돌연변이 진행 (baby_gene 값 반환)
        random_country = []
        for j in range(GA_TSP):
            gene_value = crossover_mutation(selection(GA_TSP), 0.3)
            random_country.append(gene_value)
            
        ##print('자손 :', random_country)
        ##print(i+1, '번')
        print(f"print{random_country} test")
        global test
        test = copy.deepcopy(random_country)
        print(f"test:{test}")
        sum_value_2(GA_TSP, test) #세대 적합도 구하는 함수 (score_list 값 반환)

a = play(3)
print(f"a : {a}")