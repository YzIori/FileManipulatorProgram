# FileManipulatorProgram

## オプション

### reverse

inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。ディレクトリ内に outputpath で指定したファイル名と同名のファイルが存在する場合、エラーとなります。

```bash
$ python3 file_manipulator.py reverse inputpath outputpath
```

### copy

inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。ディレクトリ内に outputpath で指定したファイル名と同名のファイルが存在する場合、エラーとなります。

```bash
$ python3 file_manipulator.py copy inputpath outputpath
```

### duplicate-contents

inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。

```bash
$ python3 file_manipulator.py duplicate-contents inputpath n
```

### replace-string

inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。

```bash
$ python3 file_manipulator.py replace-string needle newstring
```
