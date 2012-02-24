(defn mergesort [ls]
  (let [parts (partition 1 ls)]
    (loop [ls ls]
      (cond
       (= (count ls) 0) '()
       (= (count ls) 1) (first ls)
       :else
       (let [fst (first ls)
             snd (second ls)]
         (recur (merge fst snd)))))))

(defn merge [left right]
  (lazy-seq
   (cond
    (not (seq left)) right
    (not (seq right)) left
    :else (let [[l & lt] left
                [r & rt] right]
            (if (< l r)
              (cons l (merge lt right))
              (cons r (merge left rt)))))))

(println (take 4 (merge [1 3 4] [2 5 6])))
