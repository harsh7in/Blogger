
## Contribution Guidelines 
- Take a look at existing issues or create your own issues.
- Claim the issue in the comment section.
- Wait for the issue to be assigned to you after which you can start working on it.
- Create a seperate Branch for every issue you are working on.
- Refer to the issue that a PR solves, so that a PR can be related to an issue.
- Create PR to specified Branch which will be promptly reviewed and suggestions would be added for improving it.
- Add proper commit messages and documentation to your code.
- Add screenshots of your implementation to help better understand the features you have implemented (must for design related PR).
- To keep youself Merge Conflict-free
```
# Configuring a remote for a fork
$ git remote -v
> origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)

$ git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git 
> origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
> upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
> upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)


# to sync fork with original repository

$ git fetch upstream
> From https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY
>  * [new branch]      master     -> upstream/master

$ git checkout master
> Switched to branch 'master'

$ git merge upstream/master

```
- If you are making multiple commits, make sure to squash the commits amd make a PR.
- Don't override "First Come, First Serve". If someone has claimed that issue, please don't ask yourself to be assigned the same.
