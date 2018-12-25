;; Lok Chi Hon
;; Assignment 2 Clojure

(defn simplify-or [l]
  (let [l (distinct l)]
    (cond
      (some true? l) true
      (= (count (rest (remove false? l))) 1) (first(rest (remove false? l)))
      (some symbol? (rest l))(remove false? l)
      :else false
      )))

(defn simplify-and [l]
  (let [l (distinct l)]
    (cond
      (some false? l) false
      (= (count (rest (remove true? l))) 1) (first(rest (remove true? l)))
      (some symbol? (rest l))(remove true? l)
      :else true
      )))

(defn simplify-not [l]
  (cond
    (some true? l) false
    (some false? l) true
    :else l
    ))

(defn bind-values [m l]
  (map (fn [i]
         (if (seq? i)
           (bind-values m i)
           (get m i i)))
       l)
  )

(defn simplify [l]
  (if (every? symbol? l)
    (cond
      (= 'or (first l)) (simplify-or l)
      (= 'and (first l)) (simplify-and l)
      :else (simplify-not l)))
  (let [l
        (if (seq? l)
          (map(fn [i]
                (if (seq? i)
                  (simplify i) i)
                )l
              )l
          )]
    (cond
      (= 'or (first l)) (simplify-or l)
      (= 'and (first l)) (simplify-and l)
      :else (simplify-not l))
    )
  )

(defn evalexp [exp bindings]
  (simplify (bind-values bindings exp))
  )