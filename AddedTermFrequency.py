import time
import matplotlib.pyplot as plt


# function for generating the ulam sequence a_1, ..., a_i
# a_1 = u, a_2 = v, a_i <= n
def generate_sequence(u, v, n):
    terms = set()
    terms.add(u)
    terms.add(v)
    for i in range(v + 1, n):
        count = 0
        for term in terms:
            if (i - term) in terms and i != term * 2:
                count += 1
            if count > 2:
                break
        if count == 2:
            terms.add(i)
    return terms


# function for generating a dictionary term_freq in which the
# key tells us the term and the key value tells us the number
# of times this term is used to generate future terms
# E.g. to generate 3, 1 is used once and 2 is used once,
# so term_freq = {1: 1, 2: 1, 3: 0}
# the term_num dict stores the term value as a key and the
# term_num as the key value
def generate_term_frequency(u, v, n):
    term_frequency = {u: 1, v: 1}
    term_number = {u: 1, v: 2}
    terms = set()
    terms.add(u)
    terms.add(v)
    count, term1, term2 = (0, 0, 0)
    for i in range(v + 1, n):
        count = 0
        for term in terms:
            if (i - term) in terms and i != term * 2:
                term1 = i - term
                term2 = term
                count += 1
            if count > 2:
                break
        if count == 2:
            terms.add(i)
            term_number[i] = len(term_number) + 1
            term_frequency[term1] += 1
            term_frequency[term2] += 1
            term_frequency[i] = 0
    print(term_frequency)
    return term_frequency, term_number


# function for graphing term frequency
# term number is plotted on the x-axis
# frequency is plotted on the y-axis
# labels are of the form "(x, y), term value"
def graph_term_frequency(u, v, n):
    term_frequency, term_number = generate_term_frequency(u, v, n)
    xs, ys, vs = ([], [], [])
    for term in term_frequency:
        # can modify this to restrict the term number(s) graphed
        if term_number[term] < 100:
            xs.append(term_number[term])
            ys.append(term_frequency[term])
            vs.append(term)
    plt.scatter(xs, ys, color="blue")
    plt.plot(xs, ys, color="green")
    for i_x, i_y, i_v in zip(xs, ys, vs):
        # can modify this to restrict which points are labeled
        if i_y > 50 or i_x == v + 3:
            plt.text(i_x, i_y, '({}, {}), {}'.format(str(i_x), str(i_y), str(i_v)))
    plt.title("Term Number vs. Frequency")
    plt.xlabel("Term Number")
    plt.ylabel("Frequency")
    plt.show()
    return plt


def main():
    t0 = time.time()
    graph_term_frequency(1, 5, 1000)
    t1 = time.time()
    total = t1 - t0
    print(total)


if __name__ == "__main__":
    main()
