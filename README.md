# va-isaac-docs
A repository for storing basic developer oriented documentation about the suite of ISAAC projects

Note that the purpose of this repository is not to provide design documentation for ISAAC - that is handled in the master ISAAC 
docbook which can be found on CollabNet:  https://csfe.aceworkspace.net/sf/wiki/do/viewPage/projects.informatics_architecture/wiki/Docbooks

Rather, this project is intended to be a simple, concise set of documentation that is geared toward developers that are trying to build
the ISAAC suite of software.

##Projects
Currently, there are 12 projects - each with its own repository - each independently versioned.

- va-isaac-docs - https://github.com/Apelon-VA/va-isaac-docs.git
  - This project
  
- va-isaac-parent - https://github.com/Apelon-VA/va-isaac-parent.git
  - Maven 'parent' pom project.  Manages dependencies for all external dependencies.
  
- va-ochre - https://github.com/Apelon-VA/va-ochre.git
  - The interfaces used throughout ISAAC
  
- va-isaac-metadata - https://github.com/Apelon-VA/va-isaac-metadata.git
  - The Terminology metadata required to bootstrap the system.  This project outputs the terminology metadata in Java, eConcept (for loading into the database)
    and XML formats.
    
- va-isaac-mojo - https://github.com/Apelon-VA/va-isaac-mojo.git
- va-newtons-cradle - https://github.com/Apelon-VA/va-newtons-cradle.git
- va-logic - https://github.com/Apelon-VA/va-logic.git
- va-query-service - https://github.com/Apelon-VA/va-query-service.git
- va-isaac-gui - https://github.com/Apelon-VA/va-isaac-gui.git
- va-solor-goods - https://github.com/Apelon-VA/va-solor-goods.git
- va-expression-service - https://github.com/Apelon-VA/va-expression-service.git
- va-isaac-gui-pa - https://github.com/Apelon-VA/va-isaac-gui-pa.git

The GitHub repositories are the primary 'work' repositories for development.  
**This is where developers should push their work.**

Each of these repositories is also mirrored onto CollabNet
into https://csfe.aceworkspace.net/sf/scm/do/listRepositories/projects.informatics_architecture/scm

The CollabNet clone URLs follow the pattern: https://**username**@csfe.aceworkspace.net/gerrit/p/**projectname**.git or alternatively
ssh://**username**@csfe.aceworkspace.net:29418/**projectname**.git

The CollabNet repositories serve as a backup, and interact with the CollabNet issue trackers.

##Maven Build Mangement


##Utility Scripts

##Eclipse Configuration Notes

##Netbeans Configuration Notes


