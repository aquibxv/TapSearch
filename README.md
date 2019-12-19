# TapSearch
Searches for paragraphs with the given word by creating a words to paragraph mappings on an inverted index.

<h3>Api end points</h3>
<b>api/index</b>  - allows user to add documents as paragraphs to be indexed or upload PDF files <br/>
<b>api/search</b> - allows user to search for words. <br/>
                    Results are documents and PDF's(top 10) which contain the given word. <br/>
<b>api/clear</b>  - clears all the indexes and the indexed documents.

<h3> How to use </h3>
- Submit documents, PDF using /api/index endpoint to index the documets and PDF's. <br/>
- after submission head over to /api/search and search for relevant words, the resultant documents will appear in serach result.<br/>

<h3> Exceptions </h3>
While submitting PDF's refrain from submitting multiple PDF's having the same name as it throws an 'multiple objects' exception <br/>





