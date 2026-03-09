def summarize_words(lines):
    # Initialize "state" variables outside the loop
    # to keep a running total across ALL lines.
    current_longest = ""
    count = 0
    
    for line in lines:
        # split() without arguments handles multiple spaces 
        # and empty strings gracefully.
        words = line.split()
        
        # Iterate through each word in the current line
        for word in words:
            # Increment the total word counter
            count += 1

            # Check if the current word is strictly longer 
            # than the longest one found so far.
            # Using '>' ensures we keep the FIRST longest word in a tie.
            if len(word) > len(current_longest):
                current_longest = word 

    # Return the final results as a tuple after 
    # all lines and words have been processed.
    return (count, current_longest)