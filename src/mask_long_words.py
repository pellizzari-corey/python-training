def mask_long_words(sentences):
    # This list will hold our final result: a list of modified sentence strings
    masked_sentences = []

    # Step 1: Outer loop - process each sentence in the input list one by one
    for sentence in sentences:
        # Step 2: Split the current sentence into a list of individual words
        # .split() without arguments handles any whitespace automatically
        words = sentence.split()
        
        # This temporary list stores the words for ONLY the current sentence
        updated_words = []

        # Step 3: Inner loop - check every word in the current sentence
        for word in words:
            # Step 4: Logic check - is the word too long?
            if len(word) > 5:
                # If longer than 5 chars, add the mask character instead
                updated_words.append("*")
            else:
                # If 5 chars or fewer, add the original word
                updated_words.append(word)

        # Step 5: Reconstruct the sentence
        # Join the list of words back into a single string, separated by spaces
        new_sentence = " ".join(updated_words)
        
        # Step 6: Store the finished sentence in our final results list
        masked_sentences.append(new_sentence)

    # Step 7: Return the completed list of sentences to the caller
    return masked_sentences