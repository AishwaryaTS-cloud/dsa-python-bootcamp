# Trie (Prefix Tree) — Simple Notes

## 1. What Is a Trie?

A **Trie** is a special tree used to store strings (usually words). Each node stores **one character**, and when you follow a path from the root to a node, you form a **prefix** or a complete word.

Example paths can form words like:

* `seem`
* `seen`
* `seat`
* `beat`

A trie makes searching words extremely fast.

---

## 2. Why Is a Trie Used?

When you type in Google suggestions like:

* s → see different options
* se → see more filtered options

This happens because Google stores words in a structure similar to a Trie.
As you move deeper:

* You eliminate all words that don’t start with those letters.
* The search space becomes smaller at every step.

This makes searching **very fast**, even for huge dictionaries.

---

## 3. Structure of a Trie Node

Each node contains:

1. A **character** (example: 's', 'e', 't')
2. An **array of 26 child pointers** (for a–z)
3. A **flag `wordEnd`** (1 if a word ends here, 0 otherwise)

### Why 26 children?

Because English has 26 letters.
Each position in the child-array corresponds to a letter.

Example:

* index 0 → 'a'
* index 1 → 'b'
* ...
* index 25 → 'z'

We get the index by:

```
index = ASCII(letter) - ASCII('a')
```

Example:

* 'e' → ASCII 101
* 'a' → ASCII 97
* 101 - 97 = 4 → store 'e' at index 4

---

## 4. How Words Are Stored

Imagine inserting "seem":

```
root
 └── s
      └── e
           └── e
                └── m (wordEnd = 1)
```

Now inserting "seen" will reuse `s → e → e` but branch at the next character.

Trie REUSES letters where possible.
This saves memory and speeds up search.

---

## 5. Word End (wordEnd Flag)

Every time a complete word finishes, set:

```
wordEnd = 1
```

If not, keep it 0.

Example:
Word list → {"seem", "seen", "seat"}

Nodes with `wordEnd = 1`:

* m (for seem)
* n (for seen)
* t (for seat)

Nodes with `wordEnd = 0`:

* s, e, e, a (because they are only prefixes)

This helps the trie identify:

* Which paths are full words
* Which paths are only partial words

Example:
If you land on node `c` and its `wordEnd = 0`, it means **"c" is not a word**, just a prefix.

---

## 6. Searching a Word in a Trie

To search "seen":

1. Start at root
2. Look for child 's'
3. From there, child 'e'
4. From there, child 'e'
5. From there, child 'n'
6. Check wordEnd:

   * If = 1 → word exists
   * If = 0 → prefix only

This search only follows the exact path — no scanning through all words.

---

## 7. Why Trie Search Is Fast

Normally, to find a word in a big dictionary (array of words):

* You compare every word → very slow for millions of words.

In a trie:

* Each step goes directly into a child node.
* At depth k, only words starting with the first k letters are considered.
* No useless comparisons.

This is why tries are used in:

* Autocomplete
* Spell checkers
* Search suggestions
* IP routing

---

## 8. Summary

* A **Trie stores strings character by character**.
* Each node has **26 possible children**.
* **wordEnd** tells if a complete word ends there.
* Searching is fast because it follows a direct path.
* Shared prefixes save memory and speed up operations.

