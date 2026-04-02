import sys

def solve():
  
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    
    n = int(input_data[0])
    words = input_data[1:]
    
    word_counts = {}
    
    order = []
    
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
            order.append(word)
        else:
            word_counts[word] += 1
            
    
    print(len(order))
    
    
    counts = [str(word_counts[word]) for word in order]
    print(" ".join(counts))

if __name__ == "__main__":
    solve()
