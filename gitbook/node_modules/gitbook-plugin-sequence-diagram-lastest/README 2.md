# Sequence Diagram Plugin for Gitbook

Install the Sequence Diagram plugin via **NPM**

```
$ npm install gitbook-plugin-sequence-diagram-lastest
```

> if you are installing globally, you may need to put `sudo` in front of the command, `sudo npm install gitbook-plugin-sequence-diagram-lastest -g`

To use the plugin in your Gitbook project, add the plugin to the `book.json` file.

```
{
    "plugins": ["sequence-diagram-lastest"]
}
```

Then, to include a sequence diagram, just wrap your definition in a "sequence" code block. For example:

    ``` sequence
    Title: Here is a title
    A->B: Normal line
    B-->C: Dashed line
    C->>D: Open arrow
    D-->>A: Dashed open arrow
    ```

Please reference the [js-sequence-diagrams](https://bramp.github.io/js-sequence-diagrams/) documentation for details on syntax.
