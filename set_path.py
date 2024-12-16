import os,site

now_dir = os.path.dirname(os.path.abspath(__file__))
site_packages_roots = []
for path in site.getsitepackages():
    if "packages" in path:
        site_packages_roots.append(path)
if(site_packages_roots==[]):site_packages_roots=["%s/runtime/Lib/site-packages" % now_dir]

for site_packages_root in site_packages_roots:
    if os.path.exists(site_packages_root):
        try:
            with open("%s/MimicBrush.pth" % (site_packages_root), "w") as f:
                f.write(
                    "%s\n%s/MimicBrush\n"
                    % (now_dir,now_dir)
                )
            break
        except PermissionError:
            raise PermissionError
