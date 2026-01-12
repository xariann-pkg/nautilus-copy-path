Name:           nautilus-copy-path
Version:        1.2
Release:        %autorelease
Summary:        Nautilus extension to copy path, URI, name or content

License:        MIT
URL:            https://github.com/xariann-pkg/nautilus-copy-path
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       nautilus-python
Requires:       python3-gobject
Requires:       python3

%description
Nautilus Copy Path is a Python extension for the Nautilus file manager
that adds context menu entries and shortcuts to copy file data.

%prep
# Matches the directory structure of the "1.2" tag archive
%autosetup -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/nautilus-python/extensions/nautilus-copy-path
install -m 0644 nautilus-copy-path.py %{buildroot}%{_datadir}/nautilus-python/extensions/
install -m 0644 nautilus_copy_path.py translation.py config.json \
    %{buildroot}%{_datadir}/nautilus-python/extensions/nautilus-copy-path/
cp -a translations %{buildroot}%{_datadir}/nautilus-python/extensions/nautilus-copy-path/

%files
%doc README.md
%license LICENSE
%{_datadir}/nautilus-python/extensions/nautilus-copy-path.py
%{_datadir}/nautilus-python/extensions/nautilus-copy-path/

%changelog
%autochangelog
