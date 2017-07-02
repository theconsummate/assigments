# Solutions to Exercise Sheet 2, Semantic Web

## 1.1 RDFS Formal Models
#### $I_1$ where *ex:machinelearning ex:likes ex:semanticweb* is true
Assumptions:

- ex:machinelearning is a ex:Person
- ex:likes to be equivalent to ex:likesBooks

Set Model:

- D = {semanticweb, john, machinelearning}
- $(ex:semanticweb)^I = semanticweb$
- $(ex:john)^I = john$
- $(ex:machinelearing)^I = machinelearing$
- $(ex:Person)^I = \{john, machinelearing\}$
- $(ex:Reader)^I = \{john, machinelearing\}$
- $(ex:Reader)^I \subseteq (ex:Person)^I$
- $(ex:likesBook)^I \subseteq (ex:likes)^I$
- $(ex:likesBook)^I = \{(john, semanticweb)\}$

The given triple is true because ex:likes is a relationship from ex:Person to ex:Textbook and in the model specified above, ex:machinelearning is a ex:Person and ex:semanticweb: is a ex:Textbook. The relationship therefore holds.

#### $I_2$ where *ex:machinelearning ex:likes ex:semanticweb* is false
Assumptions:

- ex:machinelearning is a ex:Textbook
- ex:likes is a superclass of ex:likesBooks because the latter can be considered as a specific case of the former.
- ex:likes has the same constraint as that of ex:likesBook

Set Model:

- D = {semanticweb, john, machinelearning}
- $(ex:semanticweb)^I = semanticweb$
- $(ex:john)^I = john$
- $(ex:machinelearing)^I = machinelearing$
- $(ex:Person)^I = \{john\}$
- $(ex:Reader)^I = \{john\}$
- $(ex:Reader)^I \subseteq (ex:Person)^I$
- $(ex:Textbook)^I = \{semanticweb, machinelearning\}$
- $(ex:likesBook)^I = \{(john, semanticweb)\}$

The give triple does not hold as the contraint on ex:likes does not hold because the domain of ex:likes is ex:Person whereas ex:machinelearning is ex:Textbook.


#### ex:machinelearning ex:likes ex:semanticweb is not entailed by $O_b$ because:
- ex:machinelearning be considered to have a rdf:type of ex:Textbook.
- ex:likes can be inferred as being similar to ex:likesBook which has a rdfs:range of ex:Textbook and a rdfs:domain of ex:Person.
- Therefore the given relation *ex:machinelearning ex:likes ex:semanticweb* is not entailed because ex:machinelearning is of rdf:type ex:Textbook whereas by definition of the constraint ex:likes, it is required to be of rdf:type ex:Person.


## 1.2 Soundness of rules
#### RDFS range rule
Assume the following triples:

- ex:p rdfs:domain ex:A
- ex:X ex:p ex:Y

Let (I, $.^iI$) be an arbitary model, then it follows that

1. $Dom(p^I) \subseteq (ex:A)^I$
2. $((ex:X)^I, (ex:Y)^I) \in (ex:p)^I$

Therefore from 1 and 2, it follows that $(ex:X)^I \in (ex:A)^I$ which is the triple *ex:X rdf:type ex:A*.

#### RDFS domain rule
Assume the following triples:

- ex:p rdfs:range ex:B
- ex:X ex:p ex:Y

Let (I, $.^iI$) be an arbitary model, then it follows that

1. $Ran(p^I) \subseteq (ex:A)^I$
2. $((ex:X)^I, (ex:Y)^I) \in (ex:p)^I$

Therefore from 1 and 2, it follows that $(ex:Y)^I \in (ex:B)^I$ which is the triple *ex:Y rdf:type ex:B*.

#### RDFS subclass transitivity rule
Assume the following triples:

- ex:A rdfs:subClassOf ex:B
- ex:B ex:subClassOf ex:C

Let (I, $.^iI$) be an arbitary model, then it follows that

1. $(ex:A)^I \subseteq (ex:B)^I$
2. $(ex:B)^I \subseteq (ex:C)^I$

Therefore from 1 and 2, it follows that $(ex:A)^I \subseteq (ex:C)^I$ which is the triple *ex:A rdfs:subClassOf ex:C*.

#### RDFS subproperty rule
Assume the following triples:

- ex:subp rdfs:subPropertyOf ex:p
- ex:X rdfs:subp ex:Y

Let (I, $.^iI$) be an arbitary model, then it follows that

1. $(ex:subp)^I \subseteq (ex:p)^I$
2. $((ex:X)^I, (ex:Y)^I) \in (ex:subp)^I$

Therefore from 1 and 2, it follows that $((ex:X)^I, (ex:Y)^I) \in (ex:p)^I$ which is the triple *ex:X ex:p ex:Y*.

## 2.3.1
#### Write a new query that shows all companies residing in Stuttgart.
```sql
prefix dbo: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?company, ?locationCity WHERE {
?company a dbo:Company .
?company dbo:locationCity ?locationCity .
?locationCity rdfs:label "Stuttgart"@de.
}
```


#### Extend the query to list the homepage property of each company.
```sql
prefix dbo: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?company, ?locationCity, ?homepage WHERE {
?company a dbo:Company .
?company dbo:locationCity ?locationCity .
?locationCity rdfs:label "Stuttgart"@de.
?company dbp:homepage|foaf:homepage ?homepage .
}
```

#### Extend the query to list the foundingYear property of each company.
```sql
prefix dbo: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?company, ?locationCity, ?homepage, ?foundingYear WHERE {
?company a dbo:Company .
?company dbo:locationCity ?locationCity .
?locationCity rdfs:label "Stuttgart"@de.
?company dbp:homepage|foaf:homepage ?homepage .
?company dbo:foundingYear ?foundingYear
}
```

## 2.3.2
#### Write a query that lists films along with their director and the director's year of birth. Limit the result to 10,000 entries and list them in alphabetical order of the directors' names.
```sql
prefix dbo: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?film ?director ?birthyear
WHERE {
?film rdf:type dbo:Film .
?film dbo:director ?director .
?director dbo:birthYear ?birthyear .
} ORDER BY ?director LIMIT 10000 OFFSET 0
```

#### List all films starring John Wayne along with their runtimes. Sort the result in descending order so that the longest film is the first and the shortest film is the last entry.
```sql
prefix dbo: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?film ?starring ?runtime
WHERE {
?film rdf:type dbo:Film .
?film dbo:starring ?starring .
?starring rdfs:label "John Wayne"@en .
?film dbo:runtime ?runtime
} ORDER BY DESC(?runtime)
```

#### Edit the previous query so that only films with a runtime of more than 4,000 seconds are listed.
```sql
prefix dbo: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?film ?starring ?runtime
WHERE {
?film rdf:type dbo:Film .
?film dbo:starring ?starring .
?starring rdfs:label "John Wayne"@en .
?film dbo:runtime ?runtime .
FILTER(?runtime > 4000)
} ORDER BY DESC(?runtime)
```
