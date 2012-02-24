(defn mergesort [ls]
  (lazy-seq
   (let [[fst & rst] ls]
     (if (empty? rst)
       fst
       (let [[left right] (split-at (/ (count ls) 2) ls)]
         (merge (mergesort left) (mergesort right)))))))

(defn merge [left right]
  (lazy-seq
   (cond
    (empty? left) right
    (empty? right) left
    :else (let [[l & lt] left
                [r & rt] right]
            (if (< l r)
              (cons l (merge lt right))
              (cons r (merge left rt)))))))

(println (take 4 (merge [1 3 4] [2 5 6])))
(println (mergesort [1 6 4 2 1 6 9 2 8]))
