# va-isaac-docs
A repository for storing basic developer oriented documentation about the suite of ISAAC projects

Note that the purpose of this repository is not to provide design documentation for ISAAC - that is handled in the master ISAAC 
docbook which can be found on CollabNet:  https://csfe.aceworkspace.net/sf/wiki/do/viewPage/projects.informatics_architecture/wiki/Docbooks

Rather, this project is intended to be a simple, concise set of documentation that is geared toward developers that are trying to build
the ISAAC suite of software.

##Projects
Currently, there are 12 projects - each with its own repository - each independently versioned.

- va-isaac-docs - https://github.com/Apelon-VA/va-isaac-docs.git
  - This project - developer documentation
  
- va-isaac-parent - https://github.com/Apelon-VA/va-isaac-parent.git
  - Maven 'parent' pom project.  Manages dependencies for all external dependencies.
  
- va-ochre - https://github.com/Apelon-VA/va-ochre.git
  - The interfaces used throughout ISAAC
  
- va-isaac-metadata - https://github.com/Apelon-VA/va-isaac-metadata.git
  - The Terminology metadata required to bootstrap the system.  This project outputs the terminology metadata in Java, eConcept (for loading into the database)
    and XML formats
    
- va-isaac-mojo - https://github.com/Apelon-VA/va-isaac-mojo.git
  - Maven Mojo extensions which are used in other ISAAC projects, below, such as tooling for building a database.
  
- va-newtons-cradle - https://github.com/Apelon-VA/va-newtons-cradle.git
  - The datastore implementation for the OCHRE API.
  
- va-logic - https://github.com/Apelon-VA/va-logic.git
  - The classifier implementation for the OCHRE API
  
- va-query-service - https://github.com/Apelon-VA/va-query-service.git
  - The Query Service implementation, which includes Lucene full-text indexing capabilities
  
- va-isaac-gui - https://github.com/Apelon-VA/va-isaac-gui.git
  - A graphical front end for the ISAAC framework
  
- va-solor-goods - https://github.com/Apelon-VA/va-solor-goods.git
  - Tooling to construct a datastore (newtons cradle) and a set of indexes (query-service) and publish the resulting artifacts for consumption
  
- va-expression-service - https://github.com/Apelon-VA/va-expression-service.git
  - An demo project that shows how to start an ISAAC service and run various queries against the system.
  
- va-isaac-gui-pa - https://github.com/Apelon-VA/va-isaac-gui-pa.git
  - The *Assembly* project which is used to construct a GUI application for the end user.  While this project contains no code, it contains the 
    configuration for the assembly (things like users, change set repository location, etc) and the dependency set for the GUI (which GUI components
    should be included in the application).  It also contains the configuration for which datastore should be packaged with the GUI, and the installer
    configuration.  The end result of building this project is a GUI application for the end user - which includes all necessary components for 
    the stack above.

The GitHub repositories are the primary 'work' repositories for development.  
**This is where developers should push their work.**

Each of these repositories is also mirrored onto CollabNet
into https://csfe.aceworkspace.net/sf/scm/do/listRepositories/projects.informatics_architecture/scm

The CollabNet clone URLs follow the pattern: https://**username**@csfe.aceworkspace.net/gerrit/p/**projectname**.git or alternatively
ssh://**username**@csfe.aceworkspace.net:29418/**projectname**.git

The CollabNet repositories serve as a backup, and interact with the CollabNet issue trackers.

##Maven Build Mangement
Each project is managed and built by Maven.  Most projects are multi-module projects themselves, having multiple modules.  

In general, the necessary external dependencies to build the ISAAC suite should all be available on public repositories.  However, the terminology 
files used by the server are not publicly available.  

An Archiva server is hosted at https://va.maestrodev.com/archiva/repository/all/ for ISAAC development.  This server mirrors all necessary 
third-party libraries.  In addition, this server contains the access-restricted terminology files.  For this reason, you need credentials 
for the Archiva server to download some resources.

The example **[resources/settings.xml](https://raw.githubusercontent.com/Apelon-VA/va-isaac-docs/master/resources/settings.xml)** file in this project 
can be placed as specified by maven: https://maven.apache.org/settings.html in order to redirect your maven dependency requests through the ISAAC archiva server.  
The example file also requires your credentials for ISAAC Archiva server.

Modify this section of settings.xml as necessary:
```
<server>
    <id>maestro</id>
    <username>_YOUR_MAESTRODEV_USERNAME_</username>
    <password>_YOUR_MAESTRODEV_PASSWORD_</password>
</server>
```


##Utility Scripts

##Eclipse Configuration Notes

##Netbeans Configuration Notes


