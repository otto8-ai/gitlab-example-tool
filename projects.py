import gitlab
import os
from typing import Optional

class GitLabClient:
    def __init__(self, url: str = "https://gitlab.com", token: Optional[str] = None):
        """Initialize GitLab client
        
        Args:
            url: GitLab instance URL
            token: Private token or OAuth token. If None, looks for GITLAB_TOKEN env variable
        """
        self.token = token or os.getenv("GITLAB_OAUTH_TOKEN")
        if not self.token:
            raise ValueError("GitLab token is required. Set GITLAB_OAUTH_TOKEN env variable or pass token to constructor")
        
        self.gl = gitlab.Gitlab(url=url, private_token=self.token)
    
    def list_owned_projects(self):
        """List projects owned by the authenticated user"""
        return self.gl.projects.list(owned=True)
    
    def list_all_visible_projects(self, search: Optional[str] = None):
        """List all projects visible to the authenticated user
        
        Args:
            search: Optional search query to filter projects
        """
        return self.gl.projects.list(search=search)

def main():
    # Create client instance
    client = GitLabClient()
    
    # List owned projects
    print("Your projects:")
    for project in client.list_owned_projects():
        print(f"- {project.name} ({project.web_url})")
    
    # Example of searching for projects
    # search_term = "python"
    # print(f"\nProjects matching '{search_term}':")
    # for project in client.list_all_visible_projects(search=search_term):
    #     print(f"- {project.name} ({project.web_url})")

if __name__ == "__main__":
    main()