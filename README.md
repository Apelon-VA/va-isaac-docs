# va-isaac-docs
A repository for storing basic developer oriented documentation about the suite of ISAAC projects

Note that the purpose of this repository is not to provide design documentation for ISAAC - that is handled in the master ISAAC 
docbook which can be found on CollabNet:  https://csfe.aceworkspace.net/sf/wiki/do/viewPage/projects.informatics_architecture/wiki/Docbooks

Rather, this project is intended to be a simple, concise set of documentation that is geared toward developers that are trying to build
the ISAAC suite of software.

If you need a summary of the types of changes that have occurred with the migration away from the OTF APIs, see 
https://github.com/Apelon-VA/va-isaac-docs/blob/master/OTFMigration.md

##Requirements
ISAAC requires modern supporting software - this means Java 8, and Maven 3.x or newer.  

##Projects
Currently, there are 12 projects - each with its own repository - each independently versioned.  Note, the order here is also the order
the projects need to be built in, if you want to build the entire code stack.

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
- va-solor-goods - https://github.com/Apelon-VA/va-solor-goods.git
  - Tooling to construct a datastore (newtons cradle) and a set of indexes (query-service) and publish the resulting artifacts for consumption
- va-isaac-gui - https://github.com/Apelon-VA/va-isaac-gui.git
  - A graphical front end for the ISAAC framework
- va-isaac-gui-pa - https://github.com/Apelon-VA/va-isaac-gui-pa.git
  - The *Assembly* project which is used to construct a GUI application for the end user.  While this project contains no code, it contains the 
    configuration for the assembly (things like users, change set repository location, etc) and the dependency set for the GUI (which GUI components
    should be included in the application).  It also contains the configuration for which datastore should be packaged with the GUI, and the installer
    configuration.  The end result of building this project is a GUI application for the end user - which includes all necessary components from 
    the stack above.
- va-expression-service - https://github.com/Apelon-VA/va-expression-service.git
  - A demo project that shows how to start an ISAAC service and run various queries against the system.

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
A few utility scripts are available in the **[scripts](https://github.com/Apelon-VA/va-isaac-docs/tree/master/scripts)** sub-folder.  The scripts published
so far are all [python](https://www.python.org/) scripts which aid in management of all of the projects that make up the ISAAC suite.

To use these scripts, copy them into the same folder that contains all of your checked out ISAAC projects (likely, the parent folder of this project)

- cloneAll.py - Executes **git clone --branch 'branchname'** to pull down all of the project code from GitHub

- buildAll.py - Executes **mvn -e clean install** or **mvn -e clean package** on each project *in the correct order* to effect a complete build of the entire
ISAAC suite.

- cleanAll.py - Executes **mvn clean** on each project to recover disk space

- fetchAll.py - Executes **git fetch** on each project

- pushToCN.py - Executes **git fetch** followed by **git push** on each project, to effect synchronizing commits from the GitHub repositories to the CollabNet 
  repositories.
  

##Development Notes
Developers that are focusing on GUI development for ISAAC do not need to build all 11 of these projects locally - it will work fine to only clone
- va-isaac-gui
- va-isaac-gui-pa

For development purposes.  All other ISAAC artifact dependencies are published on the ISAAC Archiva server, and should be downloaded automatically by maven
as necessary.

However, having the full set of projects locally can be useful for debugging.

##Eclipse Configuration Notes
Eclipse 4.4 or newer is required for Java 8 support.

Eclipse [M2E](http://eclipse.org/m2e/) supports most aspects of our maven configuration files.  Upon initial import, a number of errors will occur.

###Importing Projects
The default integration of Git into eclipse does not clone into the workspace folder.  It is easier to work with the projects if you change this.

In Window -> Preferences -> Team -> Git -> Default repository folder: - change that to your workspace location or **${workspace_loc}**

Then:

- Clone the projects you want to work on with Git - do not import into the workspace yet.
- Import -> Maven -> Existing Maven Projects
  - Select the project that you checked out
  - It is also useful to "Add projet(s) to working set" at the time that you do the import
  
In the package explorer, you can then choose "Top Level Elements" from the 'Triangle' drop down menu, and change it to "Working Sets".  This will 
give you a much better hierarchial view of the maven project structures.

###M2E Lifecycle issues
You should install any M2E plugins that are available to handle lifecycle configurations, so that things such as JaxB code generation work 
correctly.

However, some do not have plugins available, such as 

- maven-plugin-plugin
- hk2-inhabitant-generator
- jacoco-maven-plugin
- plexus-component-metadata

These can be safely marked as "Ignore in Eclipse Preferences".  You can do this through the "quick fix" options in eclipse, or by manually editing the lifecycle-mapping-metadata.xml file for eclipse.  (Instructions below)

**Tip** Do 'Ignore in Eclipse Preferences' just once for each type of error.  Then do a Maven -> Update Projects on all of the projects - the rest of the 
duplicate lifecycle errors should go away.

Alternately, in Window -> Preferences -> Maven -> Errors/Warnings you can specify that "Plugin execution not covered by lifecycle configuration" issues can be
handled as warning instead of error.

Some lifecycle issues cannot be automatically handled by eclipse, such as:
"Artifact has not been packaged yet. When used on reactor artifact, copy should be executed after packaging: see MDEP-187."

This error can be removed by manually edinting the lifecycle file within eclipse (Window -> Preferences -> Maven -> Lifecycle Mappings -> Open...)

Add the following section:

```
    <pluginExecution>
      <pluginExecutionFilter>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-dependency-plugin</artifactId>
        <versionRange>2.10</versionRange>
        <goals>
          <goal>copy-dependencies</goal>
          <goal>unpack</goal>
        </goals>
      </pluginExecutionFilter>
      <action>
        <ignore />
      </action>
    </pluginExecution>
```

Then reload the lifecycle file, and then doing a *Maven Update Project* on projects that suffer from errors like this (such as app-assembly).

A complete  **[mappings file](https://github.com/Apelon-VA/va-isaac-docs/tree/master/resources/lifecycle-mapping-metadata.xml)** example which results in no build errors.


###Eclipse and jaxb2
The jaxb2 plugin for Eclipse does not work properly if your eclipse was launched using a JRE.

If you get an error like this:

```
Execution default of goal org.jvnet.jaxb2.maven2:maven-jaxb2-plugin:0.12.3:generate failed: A required class was 
missing while executing org.jvnet.jaxb2.maven2:maven-jaxb2-plugin:0.12.3:generate: com/sun/xml/bind/api/ErrorListener
```

You need to reconfigure eclipse to launch with a JDK.  The easiest way to do this is to edit the file **eclipse.ini**.  Add a **-vm** parameter, as shown here:

```
-startup
plugins/org.eclipse.equinox.launcher_1.3.0.v20140415-2008.jar
-vm
C:\Program Files\Java\jdk1.8.0_31\bin\javaw.exe
--launcher.library
plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.1.200.v20150204-1316
-product
```

###Maven Workspace Resolution
Sometimes when you import projects into Maven, it imports them with "Workspace Resolution" disabled.  This can lead to erroneous errors about not being able to resolve
other modules which are present in the same eclipse workspace.  Make sure Maven -> Enable Workspace Resolution is toggled.  To bulk update, enable workspace resolution, 
then delete, and reimport all of the projects as maven projects.

###Eclipse and JavaFX warnings

Eclipse currently has bugs in dealing with JavaFX code - and will produce copious warnings on classes that involve JavaFX libraries.  This issue can be 
fixed temporarily as documented here:  https://bugs.eclipse.org/bugs/show_bug.cgi?id=431067#c9

###Launching ISAAC from Eclipse
Launching ISAAC from within Eclipse is most easily done by creating a run configuration in the **app-assembly** project.

The main method is **gov.va.isaac.gui.App**.  Eclipse sometimes doesn't read the maven classpath properly when configuring a run configuration.  If this
 happens, simply add all of the ISAAC projects on the classpath tab of the Run Configuration.

Finally, you need a datastore.  Upon startup, ISAAC will try to locate the DB in the folder the JVM was launched from.  It is typically easiest to 
place a copy of the ISAAC datastore within the va-isaac-gui-pa/app-assembly folder - resulting in this hierarchy:

```
va-isaac-gui-pa
  - app-assembly
    - solor-all-1.8-SNAPSHOT-active-only.data
      + META-INF
      + object-chronicles
      + search
```

You can obtain a datastore using one of the following options:
 - **mvn clean package** the project va-isaac-gui-pa using maven.  When the build completes, a datastore will be located in the 
   va-isaac-gui-pa\app-assembly\target folder.  Move this datastore folder up one folder.
 - Download and unzip a datastore from Archiva https://va.maestrodev.com/archiva/#browse/gov.vha.solor.modules
 - Build a datastore using the  va-solor-goods project - move the resulting datastore from the va-solor-goods *target* subfolder.
 

###REQUIRED hack for having a local copy of isaac-metadata
Finally, in the project isaac-metadata/isaac-metadata-artifacts - you will need to manually edit the eclipse build path to resolve compiler errors.
This is because the M2E integration does not know how to execute the code (our custom mojo) which generates the java source files from the metadata
source files.

1. Manually run 'mvn compile' in this project.  This will create the folder **target/src/generated**
2. Add the folder isaac-metadata-artifacts/target/src/generated to the source build path in eclipse - and ensure that this folder is also exported 
  to dependent projects.

If you manually change any of the metadata in isaac-metadata - you will have to manually run **mvn compile** in this project, to produce the updated
java source for eclipse to consume.

##Netbeans Configuration Notes
You will need to add the Run configurations in Netbeans just like Eclipse. To get to the run config, click the down arrow next to dropdown menu that says "<default config>" > Customize > Run. 
- Main Class **gov.va.isaac.gui.App** 
- VM Options: **-Xmx6g -XX:+UseG1GC -XX:MetaspaceSize=100M ** 
- Working Directory: Choose the app-assembly folder from the va-isaac-gui-pa directory
Choose Build > Compile from the Category Tree
- Java Platform > Manage Java Platforms > Here you need to verify that you are using jdk1.8.0_31 and not jdk1.8.0_40 because revision 40 contains Java FX UI bugs that break ISAAC's GUI. You may need to Add a Platform and choose the folder that contains revision 31. You can download that from that Java Download Archives if you don't already have it.

When saving run configurations I found it finicky as they sometimes would not save, and I would have to kep re-adding them.

To enable use of the big green play buton, you must choose the ISAAC Application Assembly module from the "ISAAC Project Assembly Parent" project and Right Click > Set as Main Project.

##Required HEAP size for running with a DB
ISAAC currently requires at least 5 GB of java HEAP to run with the full SNOMED database.  To run with the full SOLOR database, you need at least
6 GB of HEAP.  Unless your system has more than 24 GB of RAM, the default JVM max for the HEAP will be inadequate - as the JVM selects 1/4 of your 
RAM as the default max.  

Furthermore, two other options (below) further improve performance.

The recommended configuration to pass into the JVM launch is:

```
-Xmx6g -XX:+UseG1GC -XX:MetaspaceSize=100M
```

Setting a larger HEAP size is encouraged, if you have a proper development system :)

The G1GC setting enables a newer garbage collector that does a better job at preventing long pauses in the GUI.  The MetaspaceSize parameter is required
to prevent a long pause during the initial usage of the GUI.  These parameters are automatically set when an end user installs ISAAC, and are included in 
the command-line launch scripts.  It is only when running within an IDE environment that you need to manually specify them.

##Logging Configuration
The logging system is configured by the file **va-isaac-gui-pa/config/src/main/resources/log4j2.xml**.  By default, two log files are produced - 
isaac.log and isaac-debug.log.  These will appear in the folder where the JVM was launched from (typically va-isaac-gui-pa/ app-assembly).

To configure so that debug or info level logging appears on the console for development purposes, uncomment the following lines in the log4j2.xml file:

```
    <!--AppenderRef ref="STDOUT-DEBUG" /-->
    <!--AppenderRef ref="STDOUT-INFO" /-->
```

##Continuous Integration
A continuous integration server is setup on MaestroDev:  https://va.maestrodev.com/projects/25 
Any push of code to GitHub automatically triggers a build of the project, in addition to any projects that depend on the changed project.  The resulting
artifacts from all of the built projects are released as new SNAPSHOT versions on the ISAAC Archiva server when the build completes.
