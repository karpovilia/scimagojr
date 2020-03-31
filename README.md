## scimagojr

Tiny script for downloading scimaojr journals rating. The main project downloads journals and their meta, given the list of science areas. 
All industries along with their codes can be found in [areas.json](https://github.com/karpovilia/scimagojr/blob/master/areas.json) file.

Data for March 31, 2020 can be found [here](https://dl.dropbox.com/s/06ni77wvrhukth3/scimagojr_full_2020-03-31.csv)

vscode `launch.json` example:
```
{
    "version": "0.0.3",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "/home/alena/repos/scimagojr/src/__main__.py",
            "console": "integratedTerminal",
            "args": [
                "--dir=/home/alena/repos/scimagojr/",
                "--areas=areas.json",
            ],
        }
    ]
}
```

Example of resuling csv filtering can be found at [analysis.ipynb](https://github.com/karpovilia/scimagojr/blob/master/analysis.ipynb)

Resulting table shows journals and conferences, that present both in computer science and linguistics fields

| Title |  Type | Q_ling_min | Q_ling_max | Q_cs_min | Q_cs_max |
| --- |  - | - | - |  ---------- | ---------- |
|2009 IEEE International Technology Management Conference, ICE 2009|conference and proceedings|4|4|4|4|
|2015 5th International Conference on Digital Information Processing and Communications, ICDIPC 2015|conference and proceedings|4|4|4|4|
|2015 IEEE 7th International Workshop on Managing Technical Debt, MTD 2015 - Proceedings|conference and proceedings|4|4|4|4|
|2015 IEEE Conference on Wireless Sensors, ICWiSE 2015|conference and proceedings|4|4|4|4|
|2015 IRCOBI Conference Proceedings - International Research Council on the Biomechanics of Injury|conference and proceedings|4|4|4|4|
|2015 International Symposium on Intelligent Signal Processing and Communication Systems, ISPACS 2015|conference and proceedings|4|4|4|4|
|ACM International Conference Proceeding Series|conference and proceedings|4|4|4|4|
|Applied Ontology|journal|1|1|1|1|
|Argument and Computation|journal|1|1|2|2|
|CALL-EJ|journal|2|2|4|4|
|Computational Linguistics|journal|1|1|2|2|
|Computational Linguistics in the Netherlands Journal|conference and proceedings|4|4|4|4|
|Computer Assisted Language Learning|journal|1|1|1|1|
|Computers and Composition|journal|1|1|1|1|
|Digital Scholarship in the Humanities|journal|2|2|3|3|
|ICCSE 2016 - 11th International Conference on Computer Science and Education|conference and proceedings|4|4|4|4|
|International Journal of Computer-Assisted Language Learning and Teaching|journal|2|2|4|4|
|JALT CALL Journal|journal|2|2|4|4|
|Journal of Logic, Language and Information|journal|2|2|2|2|
|Journal of Visual Languages and Computing|journal|2|2|3|3|
|Komp'juternaja Lingvistika i Intellektual'nye Tehnologii|conference and proceedings|4|4|4|4|
|Language Documentation and Conservation|journal|1|1|3|3|
|Language Learning and Technology|journal|1|1|1|1|
|Perspective Technologies and Methods in MEMS Design, MEMSTECH 2015 - Proceedings of 11th International Conference|conference and proceedings|4|4|4|4|
|Pragmatics and Cognition|journal|2|2|3|3|
|Proceedings of 2016 8th International Conference on Information Technology and Electrical Engineering: Empowering Technology for Better Future, ICITEE 2016|conference and proceedings|4|4|4|4|
|Procesamiento de Lenguaje Natural|journal|2|2|3|3|
|ReCALL|journal|1|1|1|1|
|Speech Communication|journal|1|1|2|2|
|Synthesis Lectures on Human Language Technologies|book series|1|1|2|2|
|TAL Traitement Automatique des Langues|journal|3|3|4|4|
|Texto Livre|journal|4|4|4|4|