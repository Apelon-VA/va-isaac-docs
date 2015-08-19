#OTF Migration
Notable changes in the APIs when moving from the OTF / TCC / Trek based APIs to the new OCHRE APIs backed by the cradle datastore

- Sememes (static and dynamic) are now stored completely differently.  There is no longer any distinction between "member" style and 
"annotation" style.  Internally, the sememes are stored completely independently of the component that they are attached to.  However,
they are also not attached to the sememe concept either - so neither member nor annotation style.  The existing legacy APIs will will
return the same values for calls that previously only returned annotation style, or member style.  The existing legacy APIs will be removed
ASAP.
  - This also means that the datastore can now natively enumerate the members of any sememe (while previously, it could only enumerate member
    style sememes - and we often used lucene indexes to enumerate annotation style sememes)

- Identifiers - previously - there were two primary identifiers in the datastore - UUIDs and NIDs.  Now, there is a third type of identifier.
  - UUID - same as previous - identifier for external use
  - NID - same as previous - a map is kept that maps between UUIDs, and NIDs - which are always negative integer values.  NIDs are invalid outside
    of the datastore enviornment that they were created in - as they are mapped during DB build time - and there is no consistent mapping from UUID
    to NID.  A NID can represent ANY type of component in the DB - so - a NID might resolve to a description, or it might resolve to a Concept, etc.
  - Sequence - a new type of identifier introduced in the OCHRE API - a sequence identifier is a positive integer.  Sequences are 'typed' - so a 
    concept sequence is different from a sememe sequence, for example.  Passing a sememe sequence identifier into an API that asks for a concept sequence
    (even though they are both integers) will result in an error, or random behavior.  Sequences are very useful for iterating over all of the components
    of a particular type (ask for the stream of concept sequence identifiers) and processing them with the Java 8 Stream APIs:
    https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html allows for easy pipelines, parallel processing, and many other advantages.
    - Note that because streams and nids are both typed as an integer, but one is positive, and one is negative - the API is flexible in many places.
      Passing in a concept stream identifier to an API that expects a NID identifier (for a concept) will work correctly, as the code will identify that 
      the value is greater than 0, and translate the concept stream ID into a NID automatically. 
    - Likewise, you can pass NIDs into APIs that expect a sequence identifier, and it will translate appropriately.  However, runtime errors will result
      if a NID that represents a Concept is passed into an API that expects a sememe sequence identifier, for example.
      
## OCHRE Model Migration

- The codebase currently only supports the OCHRE concept model.  All references to things from the org.ihtsdo packages should be considered deprecated, and removed.
- Many of the org.ihtsdo APIs no longer work correctly.  They will not be fixed - convert over to corresponding gov.vha.ochre APIs


- va-isaac-metadata has a new module now - you will likely need to import this into eclipse
This new module contains utility code that needs to exist in the dependency chain AFTER the OCHRE APIs and the metadata construction - but BEFORE implementation code, like va-newtons-cradle.  It provides a home for utility methods that are not DB implementation specific.

- va-isaac-gui has one less module now ("constants") - if eclipse still has remnants of it, you can delete it
- The build order has been slightly tweaked - va-solor-goods no longer has a dependency on va-isaac-gui - I've updated the python scripts to match (that said, there is nothing wrong with continuing to build va-isaac-gui before va-solor-goods

API changes:

- Anything related to DynamicSememe / DynamicRefex  has been redone using the ochre APIs, and a more consistent naming convention.  DynamicSememe no longer exists in the old tcc APIs (as it was completely broken anyway)

- The OTF_Concept_Model has been removed (but left the framework in place, in case we ever need to migrate to another concept model)

- The APIs into the lucene query indexes have changed.  There have been significant changes to how content is indexed to align with the ochre concept model.  In general, the index is much more powerful now.  There are currently 3 indexes - one that handles descriptions (SememeType Description), one that handles Dynamic Sememes - any of the attached column(s) - and one that handles other SememeTypes - STRING and LONG for now - with the latter handling things like SCTIDs.  The query API now allows  you to restrict a search by the Sememe Assemblage - so you can search within the Sememe Index for things of type SNOMED_INTEGER_ID

