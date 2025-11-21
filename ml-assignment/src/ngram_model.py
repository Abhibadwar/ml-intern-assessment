import random
import re
from collections import defaultdict

class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        self.trigram_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        self.bigram_counts = defaultdict(lambda: defaultdict(int))
        self.start_token = "<START>"
        self.end_token = "<END>"
        self.unk_token = "<UNK>"

    def _clean_text(self, text):
        """Clean and tokenize text."""
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s\.]', '', text)
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        return sentences

    def fit(self, text):
        """
        Trains the trigram model on the given text.
        """
        if not text.strip():
            return
            
        sentences = self._clean_text(text)
        
        for sentence in sentences:
            words = sentence.split()
            if len(words) < 1:
                continue
                
            # Add padding
            padded_words = [self.start_token, self.start_token] + words + [self.end_token]
            
            # Count trigrams and bigrams
            for i in range(len(padded_words) - 2):
                w1, w2, w3 = padded_words[i], padded_words[i+1], padded_words[i+2]
                self.trigram_counts[w1][w2][w3] += 1
                self.bigram_counts[w1][w2] += 1

    def generate(self, max_length=50):
        """
        Generates new text using the trained trigram model.
        """
        if not self.trigram_counts:
            return ""
            
        words = [self.start_token, self.start_token]
        
        for _ in range(max_length):
            w1, w2 = words[-2], words[-1]
            
            if w1 not in self.trigram_counts or w2 not in self.trigram_counts[w1]:
                break
                
            # Get possible next words and their counts
            next_words = self.trigram_counts[w1][w2]
            if not next_words:
                break
                
            # Convert counts to probabilities and sample
            total_count = sum(next_words.values())
            rand_val = random.uniform(0, total_count)
            
            cumulative = 0
            next_word = None
            for word, count in next_words.items():
                cumulative += count
                if rand_val <= cumulative:
                    next_word = word
                    break
                    
            if next_word == self.end_token:
                break
                
            words.append(next_word)
        
        # Remove start tokens and join
        generated_words = [w for w in words[2:] if w != self.end_token]
        return ' '.join(generated_words)
