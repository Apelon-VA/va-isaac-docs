# Database Source processing

The following projects are used to process native source content into the form used by ISAAC.

## Projects
- va-term-convert-common-base - https://github.com/Apelon-VA/va-term-convert-common-base
  - Shared utility code to aid in building ISAAC Representations of external terminologies (used by LOINC and RxNorm tooling)
- va-term-convert-loinc - https://github.com/Apelon-VA/va-term-convert-loinc
  - Converts LOINC from native to an ISAAC form suitable for va-solor-goods
- va-term-convert-rxnorm - https://github.com/Apelon-VA/va-term-convert-rxnorm
  - Converts RxNorm from native to an ISAAC form suitable for va-solor-goods
- va-term-convert-rf2 - https://github.com/Apelon-VA/va-term-convert-rf2
  - Converts RF2 formats (SNOMED, Extensions) from native to an ISAAC form suitable for va-solor-goods
  
  
## Per-Project Details
Each of the projects above follows the pattern:


- [term]-src-data
  - Used for uploading the native source format, exactly as it was released, into the maven artifact repository.  See the included 
  readme file for instructions on use.  No tagging / releasing is done based on work in this folder - it is only used as way to upload
  the source content as an artifact with the correct format and version information.
- [term]-mojo
  - The code that does the conversion from native source format into eConcept, suitable for ISAAC.  This code is released and managed 
  via gitflow.  Due to the nature of the converters, however, this isn't configured on the build server.  See the included ReadMe.md file
  for details on doing a release. 
- [term]-econcept
  - Contains a configuration that executes the mojo above, on the source uploaded further above.  The resulting artifact is the jbin file
  containing eConcepts suitable for loading into ISAAC via va-solor-goods.  No tagging / releasing is done based on work in this folder - 
  it is only used as a way to execute the conversion, and upload the resulting artifact with the correct format and version information.  See
  the included ReadMe.md for details on deploying the resulting artifact.
  
## Conversion Output
- Each output file is a zip file - however the type when requesting them in maven in "jbin.zip", rather than just "zip".
- Each zip file contains:
  - The jbin artifact
  - a META-INF folder
    - License / Manifest / Notice files 
    - **maven** folder
      - The maven folder contains the entire maven structure necessary to reproduce this _exact_ artifact.  The means that is provides a complete
      record of all of the software and content artifacts that were used to produce the jbin file.
  
## RF2 Notes
The rf2 converter project has multiple folders under the rf2-src-data and rf2-econcept folders - as there are configurations for each RF2 release
that is currently being converted.  At the moment, only SNOMED CT and the US Extension have been configured.  Others may be configured in the future.

The mojo code in this project was extracted / migrated from the legacy trek / workbench projects.  Class names / mojo names are the same, but the 
package structure, and upstream dependencies are not (this depends on ochre, not trek) 


