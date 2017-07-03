# Solutions to Exercise Sheet 3, Semantic Web
fully 3,4,2(owl--partially)

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

## 3. Equivalence
### 3.1 OWL DL Equivalence

### 3.2 SPARQL Equivalence
1. **Not Equivalent**: The two queries are not equivalent because if there are duplicate records in the database, the second query will return only unique values whereas the first query will return duplicates as well.

2. **Equivalent**: The order in which the birth year filter is applied does not matter.