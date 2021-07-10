# Sprint 1 / Note 1 / Git & Github

## Git

**Git은 버전 관리 시스템(Version-Control System)이다.** 

사진을 찍는 개념으로도 생각할 수 있다. 
프로젝트를 진행하는 중간중간에 사진을 찍어 기록을 하는 식이다. 
언제 누가 무슨 작업을 했는 지 트래킹이 가능하며, 다시 그 때로 돌아가 새로이 작업을 할 수도 있다. 

## Github

**Git을 저장하는 온라인 저장소 역할을 한다.**

온라인에 깃을 저장함으로써, 협업을 가능하게 한다.

### git init

**가장 먼저 해야 하는 것은 `git init` 명령어다.** 실행된 디렉토리에 깃을 시작하고 버전 관리를 하게 된다. 

깃을 생성 하며, `.git`이라는 폴더가 생기고, 해당 폴더를 통해 깃 버전 관리를 한다. 

앞으로 이 디렉토리를 추적(주시)하겠다라는 의미인 것 같다.

### 깃 지우기

깃을 지우려면 `.git` 폴더를 제거하면 된다. 

CLI를 통해서는 아래 명령어로도 가능하다. 

```bash
$ rm -rf .git
```

### git status

깃의 현재 상태를 보고 싶을 때 사용되는 명령어이다. 

현재 어떤 파일들을 추적하고 있는 지, 어떤 상태인지, 어떤 브랜치에서 작업하는지 등을 알 수 있다. 

```bash
$ git status
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled.png)

(현재 git이라는 폴더가 바뀌었다. 빨간색은 아직 add로 지정되지 않았음을 나타낸다.)

### git add

`git add` 는 추적하고 있던 깃들 중 어떤 파일들을 기록할 지 지정해주는 명령어이다. 

`git add`  다음에 파일의 경로를 지정해 특정 파일만 기록할 수도 있고, `.` 혹은 `-A`를 사용해 변경한 모든 파일(디렉토리 전체)를 지정할 수도 있다. 

```bash
$ git add git
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%201.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%201.png)

('git'이라는 폴더를 add로 지정했다. status를 다시 보니 초록색으로 지정되었음을 알 수 있고, 그 안에 2개의 파일이 있는 것을 알 수 있다.)

### git commit

`git init`을 통해 추적하고, `git add`를 통해 기록 여부를 정했다면, `git commit`을 통해 실제로 기록한다. 사진을 찍으려고 셔터를 누르는 행위로 볼 수 있다. 

커밋을 할 때에는 반드시 메세지를 적어야한다.

`git commit` 을 입력하면 메세지를 기록할 에디터를 열어주며, `-m` 플래그를 사용하면 에디터 없이 바로 메세지를 남길 수도 있다.

```bash
$ git commit -m "message"
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%202.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%202.png)

## Github 명령어

### git remote

`git remote` 는 Github의 레파지토리(repository, 레포, repo)와 연결하는 명령어이다. 

`-v` 플래그를 통해 현재 연결되어 있는 레포를 볼 수 있다. 

```bash
$ git remote -v
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%203.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%203.png)

(origin이란 이름으로 study-numpy-pandas라는 레포가 연결되어있다.)

깃허브 레포와 연결하고자 한다면 `git remote add`를 통해 주소를 추가해줄 수 있다. 

그 뒤에는 저장하고자 하는 이름, https주소를 쓰면 된다. 

[https://github.com/tkryu91/Study.git](https://github.com/tkryu91/Study.git)에 연결하여 study라는 이름으로 저장하고 싶다면 아래와 같이 쓸 수 있다. 

여기서 study는 단순히 해당 주소를 단축어로 지정해놓은 것이다. 

일반적으로 origin이라는 단축어를 많이 쓰며, origin 이름자체에 의미는 없다. 본인이 쓰고 싶은 이름을 쓰면 된다.

```bash
$ git remote add study https://github.com/tkryu91/Study.git
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%204.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%204.png)

(study라는 이름으로 study 레포를 추가)

연결된 주소를 지우고자 한다면 remove를 사용한다. 

```bash
$ git remote remove origin
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%205.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%205.png)

(origin은 예전 주소였으므로 삭제하고, study라는 이름만 남겨놓았다.)

### git clone, git fetch, git pull

깃허브 상의 레포를 복사해오는 명령어이다. 

**git clone :** 해당 레포를 통재로 복사한다. 

**git fetch :** 해당 레포에서 변경된 사항만 가지고 온다. (내 로컬에 있는 것보다 업데이트된 것)

**git pull :** 해당 레포를 복사해서 내가 작업한 것을 덮어씌움 (기존 git hub에 있던 것과 다른 버전에서 작업하여 버전이 달라진 경우, push가 안된다. 따라서 기존 git hub에 있던 것을 불러온 후 덮어씌움으로서 통합해주는 것 같다. 확실치 않음... 웬만하면 쓰지 않는 것이 좋다고 한다.)

```bash
git clone study
git fetch study
git pull study
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%206.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%206.png)

### git merge

브랜치를 합치는 명령어이다. 

main 브랜치가 깃헙에서 업데이트되어서 fetch로 가지고 온 후 내가 작업하던 브랜치에 덮어씌울 경우, 혹은 

내가 작업한 브랜치를 main (혹은 다른) 브랜치로 합칠 경우에 사용한다. 

**A branch에서 `git merge B` 를 실행하면 B의 내용이 A에 덮어씌워진다.**

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%207.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%207.png)

('practice'라는 branch에 main branch를 덮어씌움)

### 작업 branch 변경

`git checkout branch`이름을 통해 작업할 브랜치를 변경할 수 있다.

```bash
$ git checkout test
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%208.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%208.png)

(기존에 main에서 작업하다가 test로 작업하는 것으로 변경)

### Branch명 변경

로컬과 원격에서 적용하는 방법이 다르다.

**로컬에서는 `git branch -m old_name new_name`으로 브랜치 이름을 변경한다.**

```bash
git branch -m test practice
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%209.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%209.png)

(로컬에서 기존 test라는 브랜치 이름을 practice로 변경)

**Github 상의 브랜치명을 변경하려면 바꾼 이름의 브랜치를 업로드하고, 기존의 브랜치를 삭제해야한다. 삭제하고나면 안전장치가 없으니 주의해야 한다.**

```bash
# 새로 바꾼 B를 업로드
git push study B

# 기존의 A를 삭제 (둘 중 아무거나)
git push study --delete A
git push study :A

# B 업로드와 A 삭제를 동시에
git push study :A B
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%2010.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%2010.png)

(기존의 test branch를 삭제하고 practice branch를 추가)

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%2011.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%2011.png)

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%2012.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%2012.png)

(깃허브 상에서 브랜치 명이 바뀐 것을 확인)

### git push

push는 로컬에서 작업한 것을 깃허브상으로 업로드하는 명령어이다. 

```bash
$ git push study main
```

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%2013.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%2013.png)

![Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%2014.png](Sprint%201%20Note%201%20Git%20&%20Github%20ba0b2367e2d14072a30442ff0d2c57a2/Untitled%2014.png)

(깃허브 상에 git 폴더가 생기며 업로드되었다.)