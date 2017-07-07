# Solutions to Exercise Sheet 3, Semantic Web

## 1. OWL Modelling
1. The Khumbu is a Nepalese region, a Nepalese region is a region. (ex:Khumbu, ex:NepaleseRegion, ex:Region)
- ex:Khumbu rdf:type ex:NepaleseRegion
- ex:NepaleseRegion rdfs:subClassOf ex:Region

2. When A has climbed mountain M, M has been climbed by A. (ex:hasClimbed, ex:hasBeenClimbedBy)
- ex:hasClimbed owl:inverseOf ex:hasBeenClimbedBy

3. Tenzing Norgay is a different person than Edmund Hillary. (ex:EdmundHillary, ex:TenzingNorgay)
- ex:EdmundHillary owl:differentFrom ex:TenzingNorgay

4. One thing among many that makes something an interesting mountains is that it has been climbed by Tenzing Norgay.
(ex:hasBeenClimbedBy, ex:InterestingMountain, ex:TenzingNorgay)
- ex:hasBeenClimbedBy rdf:type owl:DatatypeProperty
- ex:hasBeenClimbedBy rdfs:domain ex:InterestingMountain
- ex:hasBeenClimbedBy rdfs:range ex:TenzingNorgay

5. Mountains and cities are located in only in regions, regions are the only thing they can be located in. (ex:City, ex:locatedInRegion, ex:Mountain, ex:Region)
- ex:Region rdf:type owl:Class
- ex:locatedInRegion rdf:type owl:ObjectProperty
- ex:locatedInRegion rdfs:domain [
    rdf:type owl:Class;
    owl:unionOf (ex:Mountain ex:Region);
]
- ex:locatedInRegion rdfs:range ex:Region

6. A Nepalese Mountain is defined as something that is a mountain and it is located in one of the regions of Nepal, nothing else is a Nepalese mountain.
(ex:locatedInRegion, ex:Mountain, ex:NepaleseMountain, ex:NepaleseRegion)
- ex:NepaleseMountain rdf:type owl:Class
- ex:NepaleseMountain rdfs:subClassOf ex:Mountain, [
    rdf:type owl:Restriction;
    owl:onProperty ex:locatedInRegion;
    owl:hasValue ex:NepaleseRegion;
]

7. Use any element of OWL to say something that makes sense in this domain. Give the OWL statemtent(s) and a short textual description (1-2 sentences).
- A city can't be a mountain (ex:City, ex:Mountain)
- ex:City owl:disjointWith ex:Mountain

### 2. Protege
#### Additions to the ontology
- rdf:type Book as a superclass of Textbook
- inverse property isLikeBy of likesBook
- new class Fiction as a subclass of Book which is disjoint from Textbook.
- new instances which are different from each other.

There is inconsistency.

## 3. Equivalence
### 3.1 OWL DL Equivalence
1. ∃≥1r.A ≡ ∃r.A
- ∃≥1r.A implies the subset of A having more than at least one item satisfying the restriction. This is equivalent as having some values satisfy the restriction as implied by ∃r.A

2. ¬(¬A⊓¬B)≡A⊔B
For a given set x, the following relations hold:
- x + ¬x = U (U is the entire universe)
- x⊓¬x = ⊥

Therefore it is sufficient to prove the (A⊔B)⊔(¬A⊓¬B) = U and (A⊔B)⊓(¬A⊓¬B) = ⊥

- (A⊔B)⊔(¬A⊓¬B) = ( (A⊔B) ⊔ ¬A ) ⊓ ( (A⊔B) ⊔ ¬B )
                = (B ⊔ U) ⊓ (A ⊔ U)
                = U ⊓ U
                = U

- (A⊔B)⊓(¬A⊓¬B) = ( (¬A⊓¬B) ⊓ A) ⊔ ( (¬A⊓¬B) ⊓ B)
                = ( ¬B ⊓ ⊥) ⊔ ( ¬A ⊓ ⊥)
                = (⊥) ⊔ (⊥)
                = ⊥

3. A⊓A≡A
This is true because the intersection of a set A with itself will contain all the elements in the original set.

4. A⊓⊥ ≡ ¬(A⊔¬A)
- A⊓⊥ = ⊥
- ¬(A⊔¬A) = ¬(U) = ⊥

### 3.2 SPARQL Equivalence
1. **Not Equivalent**:
- The two queries are not equivalent because ordering is different. In the first case, the default ordering is ascending whereas in the second one, it is descending.
- The main difference is in the Order by part.

2. **Equivalent**:
- The order in which the birth year filter is applied does not matter.
- The main difference is the filter part. In first query, the explicit FILTER keyword is used whereas in the second query, equality check is used.