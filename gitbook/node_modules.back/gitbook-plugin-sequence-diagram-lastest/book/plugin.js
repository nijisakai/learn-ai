require(["gitbook"], function(gitbook) {
  gitbook.events.bind("page.change", function() {
    $('code.lang-sequence').sequenceDiagram({theme: 'simple'});
  });
});
