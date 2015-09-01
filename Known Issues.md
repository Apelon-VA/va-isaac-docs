# Known Issues

Various known issues across the ISAAC framework and other notes...

## Regressions (primarily)

- Creating new concepts / descriptions via Blueprint API is not currently updating the lucene indexes
- There is no functioning commit notification / listener mechanism
  - This breaks the existing workflow implementation
- The APIs for addUncommitted / Commit don't yet seem to be defined in enough detail 
  - no way of knowing if a addUncommitted was successful (as it runs in a background thread)
  - no return on the commit call - no way to handle errors other than IOException - what if the commit was prevented by a validation rule?
- The shutdown sequence is extremely fragile
  - Files are being written during shutdown - overwriting in place.  Any interruption corrupts the DB in a way that is unrecoverable.
    - At a minimum, it seems that the services should write out all of their files to a new file - then swap file names at the end
  - The shutdown sequence is also rather slow - leading to users killing the process - which - corrupts the DB per above.
  - The writes during shutdown make me wonder when things are actually written to disk.  Editors don't can't work with a tool that could lose all of their 
    work if something fails 4 hours into the day - and they can't run the shutdown sequence.


## Needed functionality
- SOLOR work requires the ability to merge concepts, at runtime - rather than attempting a hack / DB dump / reload to try to force them to merge.
 - There is no per-concept commit
   - We could work without this - but we need guidance - many GUI decisions need to be made on whether we will or won't have per-concept commit.
  
  
## Desired functionality
- Rather than concept based commit - I would still prefer transaction based commit - where addUncommitted returns a token - and multiple calls to addUncommited
  could be made using the same token - then committed at once.
  - Keith did express that this was very complicated due to the DB design - I don't understand enough of the details to know how hard of a thing I'm requesting.
- Memory requirements right now - for the full SOLOR bundle - are high.  Unlikely to run on typical VA class systems.
- Memory requirements for running the classifier on full SOLOR are really high.
- Startup sequence is much slower than the OTF system - perhaps reducing the memory footprint by keeping more data on disk will help this as well.

  
## General TODOs
- A bunch of JUnit tests still haven't made the transition from OTF to the ISAAC framework - need to be repaired / brought back.
- Much code needs to be ported from Blueprint APIs to Builder APIs, so we can throw out the Blueprint stuff