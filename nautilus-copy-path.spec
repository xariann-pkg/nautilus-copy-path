Name:           nautilus-copy-path
Version:        1.0
Release:        %autorelease
Summary:        Nautilus extension to copy path, URI, name or content

License:        MIT
URL:            https://github.com/Xarianne/nautilus-copy-path
# Dynamic source URL for Packit automation
Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       nautilus-python
Requires:       python3-gobject
Requires:       python3

%description
Nautilus Copy Path is a Python extension for the Nautilus file manager
that adds context menu entries and shortcuts to copy the selected file
or directory path, URI, name or file content to the clipboard[cite: 17].

%prep
# Matches the directory structure created by the versioned tag
%autosetup -n %{name}-%{name}-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/nautilus-python/extensions/nautilus-copy-path

# Install the main extension script
install -m 0644 nautilus-copy-path.py \
    %{buildroot}%{_datadir}/nautilus-python/extensions/

# Install support files and translations 
install -m 0644 nautilus_copy_path.py translation.py config.json \
    %{buildroot}%{_datadir}/nautilus-python/extensions/nautilus-copy-path/

cp -a translations \
    %{buildroot}%{_datadir}/nautilus-python/extensions/nautilus-copy-path/

%files
%doc README.md
%license LICENSE
%{_datadir}/nautilus-python/extensions/nautilus-copy-path.py
%{_datadir}/nautilus-python/extensions/nautilus-copy-path/

%changelog
%autochangelog
